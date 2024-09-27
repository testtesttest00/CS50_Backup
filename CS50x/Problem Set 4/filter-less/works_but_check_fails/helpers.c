#include "helpers.h"
#include <math.h>

int comp(int x, int y);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
    // image[height][width] does not have to be a pointer (duck debugger):
    // In C, when you pass a 2D array to a function, it decays into a pointer
    // to the first element of the array.
{
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            int8_t mean = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = mean;
            image[i][j].rgbtGreen = mean;
            image[i][j].rgbtRed = mean;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            float blue = image[i][j].rgbtBlue;
            float green = image[i][j].rgbtGreen;
            float red = image[i][j].rgbtRed;
            image[i][j].rgbtBlue = comp(round(.272 * red + .534 * green + .131 * blue), 255);
            image[i][j].rgbtGreen = comp(round(.349 * red + .686 * green + .168 * blue), 255);
            image[i][j].rgbtRed = comp(round(.393 * red + .769 * green + .189 * blue), 255);
        }
    }
    return;
}

int comp(int x, int y){ //does not need pointer as it returns a value
    if (x < y){
        return x;
    }
    else{
        return y;
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int i = 0; i < height; i++){
        for (int j = 0, iter = floor(width/2); j < iter; j++){
            //temp = image[i][j];             this mirrors image
            //image[i][width - j] = image[i][j];             ...
            //image[i][j] = temp;                            ...
            temp = image[i][width - j];
            image[i][width - j] = image[i][j];
            image[i][j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // idea: RGBTRIPLE avglist[9] -> avg(RGBTRIPLE *list) where avg is counted from every elemnt of array
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            int range_rows[3] = {i-1, i, i+1};
            int range_columns[3] = {j-1, j, j+1};
            int pixels = 0;
            int red = 0;
            int green = 0;
            int blue = 0;
            for (int x = 0; x < 3; x++){
                if (range_rows[x] >= 0 && range_rows[x] <= height){
                    for (int y = 0; y < 3; y++){
                        if(range_columns[y] >= 0 && range_columns[y] <= width){
                            red += image[range_rows[x]][range_columns[y]].rgbtRed;
                            green += image[range_rows[x]][range_columns[y]].rgbtGreen;
                            blue += image[range_rows[x]][range_columns[y]].rgbtBlue;
                            pixels++;
                        }
                    }
                }
            }
            int avgRed = round((float) red / pixels);
            temp[i][j].rgbtRed = avgRed;
            int avgGreen = round((float) green / pixels);
            temp[i][j].rgbtGreen = avgGreen;
            int avgBlue = round((float) blue / pixels);
            temp[i][j].rgbtBlue = avgBlue;
        }
    }
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            image[i][j] = temp[i][j];
        }
    }
    //image = temp; cant be used as only the pointer is swapped.
    // also, image pointer here is a temporary local pointer created when image is passed as argument
    // image -ptr-> 0x1: 0x1[image[0]] 0x2[image[1]] 0x3[image[2]]...
    // blur (x, y, 0x1){
    // temp -ptr-> 0xff1: 0xff1[temp[0]] 0xff2[temp[1]] 0xff3[temp[2]]...
    // image = temp does this: (local) 0x1 = 0xff1, (local) image = 0xff1
    //} outside, unchanged is image = 0x1, 0xff1 is deallocated and nothing is pointing to it anyway
    return;
}
