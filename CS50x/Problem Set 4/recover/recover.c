#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int FAT = 512;

int main(int argc, char *argv[]){

    if (argc != 2){
        printf("Usage: ./recover file_name\n");
        return 1;
    }

    FILE *raw = fopen(argv[1], "r");
    if (raw == NULL){
        printf("Unable to open \"%s\"\n", argv[1]);
        return 1;
    }

    uint8_t b[FAT];
    int files = 0;
    int init = 0;
    char *filename = malloc(sizeof("000.jpg"));
    FILE *file_jpg;
    //printf("%lu\n", sizeof(*file_jpg));
    // returns 216 (the size of FILE structure)
    // returns 8 if sizeof(file_jpg) is used (the size of FILE pointer)
    // use fseek ftell seek_end

    while (fread(&b, FAT, 1, raw)){
        if ((b[0] == 0xff && b[1] == 0xd8 && b[2] == 0xff) && (b[3] >= 0xe0 && b[3] <= 0xef)){
            if (init){
                fclose(file_jpg);
                //init = 0;
            }
            init = 1;
            sprintf(filename, "%.3i.jpg", files);
            file_jpg = fopen(filename, "w");
            if (file_jpg == NULL){
                printf("Unable to create \"%s\"\n", filename);
                return 1;
            }
            files++;
            fwrite(&b, FAT, 1, file_jpg);
        }
        else if (init){
            fwrite(&b, FAT, 1, file_jpg);
            //no need realloc file_jpg, OS will handle it during fwrite (besides, FILE *file_jpg = malloc(FAT) is wrong)
        }
    }

    //printf("%s closed\n", filename);
    fclose(file_jpg);
    free(filename);
    fclose(raw);
    return 0;
}
