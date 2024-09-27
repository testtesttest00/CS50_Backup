// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

//ver 1: re-done (notes @ ver 2)------------------------------------------------------------------------------------------------
    char *header = malloc(44);
    // locname:&header/varname:header/size:8[0xf...&header[0]...]
    //fread(header, sizeof(header), 44, input); // sizeof(header) = 8 byte (long type storing &header[0])
    //fwrite(header, sizeof(header), 44, output);
    //printf("%d\n", *header);
    fread(header, sizeof(*header), 44, input);
    fwrite(header, sizeof(*header), 44, output);
    free(header);

    //fread(header, sizeof(header), 44, input); // error with sizeof(header) == 8
    //fwrite(header, sizeof(header), 44, output); // 8 * 44 bytes are transferred
    //free(header); // free(): invalid pointer\n Aborted (core dumped)\n seen otherwise

//ver 2-------------------------------------------------------------------------------------------------------------------------
//    char *header;
    // locname:&header/varname:header/size:8[0xf...header(trash)...]
//    header = malloc(44);
    // locname:&header/varname:header/size:8[0xf...header(malloc44)...]
    // ----points to----> locname:&*header|&header[0]/varname:*header|header[0]//size:1[...header[0]...]

    //printf("%lu\n", sizeof(*header)); >>> 1 (size of header[0])
    //printf("%lu\n", sizeof(header)); >>> 8 (size of header, ptr to *header)
    //printf("%lu\n", sizeof(&header)); >>> 8 (size of &header)
    //printf("%lu\n", sizeof(&*header)); >>> 8 (size of &*header)
    //printf("%lu\n", sizeof(&header[0])); >>> 8 (size of &*header)

//    fread(header, 44, 1, input);
    // does not work to use sizeof(*header): *header is treated as an array of char, returns size 1 for char[0] rather than 44
//    fwrite(header, 44, 1, output);
    // 1 iteration * 44 bytes, updates buffer @ *header / header[0]
//    free(header);
    // frees memory stored @ *header / header[0]

//ver 3 (hint)------------------------------------------------------------------------------------------------------------------
//    uint8_t header[HEADER_SIZE];
//    printf("%lu\n", sizeof(header));
//    fread(&header, sizeof(header), 1, input);
//    fwrite(&header, sizeof(header), 1, output);

    // TODO: Read samples from input file and write updated data to output file

//ver 1: re-done (nothing much i could change from ver 2)-----------------------------------------------------------------------
    int16_t b;
    while (fread(&b, sizeof(b), 1, input)){
        b *= factor;
        fwrite(&b, sizeof(b), 1, output);
    }

    //if fread(sizeb, 2) & fwrite(sizeb, 1): output speeds up and pitches up by 2 (converse is true)
    //long b; fread(&b, sizeof(b), 1, input) // more noise, less change in timbre
    //long b; fread(&b, sizeof(b), 2, input) // mild noise, more change in timbre
    //double b; // generates noise + wrong factor multiplication
    // dont't use uint16_t: 0 < factor < 1 are treated as vol increase (unsigned int wrap around)
    //int8_t b;
    //while (fread(&b, sizeof(b), 1, input)){ //generates noise because 2 byte sample is copied 1 byte at a time
    //    b *= factor;
    //    fwrite(&b, sizeof(b), 1, output);
    //}

//ver 2 (hint)------------------------------------------------------------------------------------------------------------------
//    int16_t b;
    // dont't use uint16_t: 0 < factor < 1 are treated as vol increase (unsigned int wrap around)
//    while (fread(&b, sizeof(b), 1, input)){
//        b *= factor;
//        fwrite(&b, sizeof(b), 1, output);
//    }

    // Close files
    fclose(input);
    fclose(output);
}
