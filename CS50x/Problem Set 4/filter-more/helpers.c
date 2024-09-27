#include "helpers.h"
#include <math.h>
//#include <stdio.h>

int red(RGBTRIPLE *image, int y, int height, int x, int width);
int green(RGBTRIPLE *image, int y, int height, int x, int width);
int blue(RGBTRIPLE *image, int y, int height, int x, int width);
int comp(int x, int y);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
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

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int i = 0; i < height; i++){
        for (int j = 0, iter = floor(width/2); j < iter; j++){
            temp = image[i][width - 1 - j];
            image[i][width - 1 - j] = image[i][j];
            image[i][j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
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
                if (range_rows[x] >= 0 && range_rows[x] < height){
                    for (int y = 0; y < 3; y++){
                        if(range_columns[y] >= 0 && range_columns[y] < width){
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
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Method 1: Use external functions
    //
    // Allows computation of edge cases
    // with RBG 0 border using external
    // function to detect when to use 0

//    printf("%d\n%d\n",height,width);
//    RGBTRIPLE temp[height][width];
//    // Loop for each pixel
//    for (int i = 0; i < height; i++){
//        for (int j = 0; j < width; j++){
//
//            // vvv Does not work as multiple at each cell is not the same
//            // Loop around each pixel within a +1/-1 range
//            //for (int y = -1; y < 1; y++){
//            //    for (int x = -1; x < 1; x++){
//            //
//            //        // Get Red Gx
//            //        int rgx = -1(image[i+y][j+x])
//            //
//            //        // Catch edge cases
//            //        if (i + y < 0 || i + y == height){
//            //
//            //        }
//            //        if (j + x < 0 || j + x == width){
//            //
//            //        }
//            //    }
//            //}
//
//            int rgx = -red(&image[0][0],i-1,height,j-1,width) -2*red(&image[0][0],i,height,j-1,width) -red(&image[0][0],i+1,height,j-1,width) +red(&image[0][0],i-1,height,j+1,width) +2*red(&image[0][0],i,height,j+1,width) +red(&image[0][0],i+1,height,j+1,width);
//            int rgy = -red(&image[0][0],i-1,height,j-1,width) -2*red(&image[0][0],i-1,height,j,width) -red(&image[0][0],i-1,height,j+1,width) +red(&image[0][0],i+1,height,j-1,width) +2*red(&image[0][0],i+1,height,j,width) +red(&image[0][0],i+1,height,j+1,width);
//            temp[i][j].rgbtRed = comp(round(sqrt((float) pow(rgx, 2) + pow(rgy, 2))), 255);
//            int ggx = -green(&image[0][0],i-1,height,j-1,width) -2*green(&image[0][0],i,height,j-1,width) -green(&image[0][0],i+1,height,j-1,width) +green(&image[0][0],i-1,height,j+1,width) +2*green(&image[0][0],i,height,j+1,width) +green(&image[0][0],i+1,height,j+1,width);
//            int ggy = -green(&image[0][0],i-1,height,j-1,width) -2*green(&image[0][0],i-1,height,j,width) -green(&image[0][0],i-1,height,j+1,width) +green(&image[0][0],i+1,height,j-1,width) +2*green(&image[0][0],i+1,height,j,width) +green(&image[0][0],i+1,height,j+1,width);
//            temp[i][j].rgbtGreen = comp(round(sqrt((float) pow(ggx, 2) + pow(ggy, 2))), 255);
//            int bgx = -blue(&image[0][0],i-1,height,j-1,width) -2*blue(&image[0][0],i,height,j-1,width) -blue(&image[0][0],i+1,height,j-1,width) +blue(&image[0][0],i-1,height,j+1,width) +2*blue(&image[0][0],i,height,j+1,width) +blue(&image[0][0],i+1,height,j+1,width);
//            int bgy = -blue(&image[0][0],i-1,height,j-1,width) -2*blue(&image[0][0],i-1,height,j,width) -blue(&image[0][0],i-1,height,j+1,width) +blue(&image[0][0],i+1,height,j-1,width) +2*blue(&image[0][0],i+1,height,j,width) +blue(&image[0][0],i+1,height,j+1,width);
//            temp[i][j].rgbtBlue = comp(round(sqrt((float) pow(bgx, 2) + pow(bgy, 2))), 255);
//            // cant use green(image) as image points to the first element of a 2D array, but
//            // the function expects 1D array, so green(&image[0][0]) is used here instead
//
//            if (i == 0){
//                printf("width: %i\n",j+1);
//            }
//            if (j == width - 1){
//                printf("height: %i\n", i+1);
//            }
//        }
//    }
//    for (int i = 0; i < height; i++){
//        for (int j = 0; j < width; j++){
//            image[i][j] = temp[i][j];
//        }
//    }
//    return;

    // Method 2: Create bordered image
    //
    // Creates a separate image array
    // with an added border around it
    // allowing for simple iterations

    // Temporary bordered image (deallocated after)
    int b_height = height + 2;
    int b_width = width + 2;
    RGBTRIPLE b_image[b_height][b_width];
    for (int i = 0; i < b_height; i++){
        for (int j = 0; j < b_width; j++){
            if (i == 0 || j == 0 || i == b_height - 1 || j == b_width - 1){
                b_image[i][j].rgbtRed = 0;
                b_image[i][j].rgbtGreen = 0;
                b_image[i][j].rgbtBlue = 0;
            }
            else{
                b_image[i][j] = image[i-1][j-1];
            }
        }
    }
    // Tempopary border image done

    // Loop for each pixel of valid image
    for (int i = 1; i < height + 1; i++){
        for (int j = 1; j < width + 1; j++){
            int gx = -b_image[i-1][j-1].rgbtRed -2*b_image[i][j-1].rgbtRed -b_image[i+1][j-1].rgbtRed +b_image[i-1][j+1].rgbtRed +2*b_image[i][j+1].rgbtRed +b_image[i+1][j+1].rgbtRed;
            int gy = -b_image[i-1][j-1].rgbtRed -2*b_image[i-1][j].rgbtRed -b_image[i-1][j+1].rgbtRed +b_image[i+1][j-1].rgbtRed +2*b_image[i+1][j].rgbtRed +b_image[i+1][j+1].rgbtRed;
            image[i-1][j-1].rgbtRed = comp(round(sqrt((double) pow(gx, 2) + pow(gy, 2))), 255);
            gx = -b_image[i-1][j-1].rgbtGreen -2*b_image[i][j-1].rgbtGreen -b_image[i+1][j-1].rgbtGreen +b_image[i-1][j+1].rgbtGreen +2*b_image[i][j+1].rgbtGreen +b_image[i+1][j+1].rgbtGreen;
            gy = -b_image[i-1][j-1].rgbtGreen -2*b_image[i-1][j].rgbtGreen -b_image[i-1][j+1].rgbtGreen +b_image[i+1][j-1].rgbtGreen +2*b_image[i+1][j].rgbtGreen +b_image[i+1][j+1].rgbtGreen;
            image[i-1][j-1].rgbtGreen = comp(round(sqrt((double) pow(gx, 2) + pow(gy, 2))), 255);
            gx = -b_image[i-1][j-1].rgbtBlue -2*b_image[i][j-1].rgbtBlue -b_image[i+1][j-1].rgbtBlue +b_image[i-1][j+1].rgbtBlue +2*b_image[i][j+1].rgbtBlue +b_image[i+1][j+1].rgbtBlue;
            gy = -b_image[i-1][j-1].rgbtBlue -2*b_image[i-1][j].rgbtBlue -b_image[i-1][j+1].rgbtBlue +b_image[i+1][j-1].rgbtBlue +2*b_image[i+1][j].rgbtBlue +b_image[i+1][j+1].rgbtBlue;
            image[i-1][j-1].rgbtBlue = comp(round(sqrt((double) pow(gx, 2) + pow(gy, 2))), 255);
        }
    }

    return;
}

int red(RGBTRIPLE *image, int y, int height, int x, int width){
    if (y < 0 || y == height || x < 0 || x == width){
        return 0;
    }
    else{
        return (image + y * width + x)->rgbtRed;
        //return (*(image + y * width + x)).rgbtRed; also works.
        // From duck debugger:
        // The . operator has higher precedence than the * operator,
        // so you would need parentheses to dereference first:
        // (*(image + y * width + x)).rgbtGreen.
        // The -> operator simplifies this by combining dereferencing and member access.
    }
}

int green(RGBTRIPLE *image, int y, int height, int x, int width){
    if (y < 0 || y == height || x < 0 || x == width){
        return 0;
    }
    else{
        return (*(image + y * width + x)).rgbtGreen;
    }
}

int blue(RGBTRIPLE *image, int y, int height, int x, int width){
    if (y < 0 || y == height || x < 0 || x == width){
        return 0;
    }
    else{
        return (image + y * width + x)->rgbtBlue;
    }
}

int comp(int x, int y){ //does not need pointer as it returns a value
    if (x < y){
        return x;
    }
    else{
        return y;
    }
}
