#include <stdint.h>
#include <iostream>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

int main() {
    int width, height, bpp;

    uint8_t* rgb_image = stbi_load("image.png", &width, &height, &bpp, 3);

    stbi_image_free(rgb_image);

    std::cout << width << " " << height << " " << bpp << std::endl;
    return 0;
}