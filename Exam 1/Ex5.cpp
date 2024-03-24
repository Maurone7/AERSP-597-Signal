#include <iostream>
#include <stdlib.h>
#include <array>
#include <fstream>
#include <opencv2/opencv.hpp>

int main(){
    int n;
    // Number of iterations
    n = 5;
    // Threshold
    float n1 = 0.1;

    // k-means
    const size_t k = 10;

    cv::Mat image = cv::imread("../Mnm.png");

    int rows = image.rows;
    int cols = image.cols;
    int N1 = rows * cols;

    auto x1 = new int[N1];
    auto x2 = new int[N1];
    auto x3 = new int[N1];
    auto x = new int[N1][3];

    int index = 0;
    for (int i = 0; i < image.rows; i++) {
        for (int j = 0; j < image.cols; j++) {
            cv::Vec3b pixel = image.at<cv::Vec3b>(i, j);
            x1[index] = pixel[0];
            x2[index] = pixel[1];
            x3[index] = pixel[2];
            std::cout << pixel[0] << std::endl;

            index++;
        }
    }

    if (image.empty()) {
        std::cout << "Failed to read image" << std::endl;
        return -1;
    }

    for (int i = 0; i < rows; i++) {
        x[i][0] = x1[i];
        x[i][1] = x2[i];
        x[i][2] = x3[i];
    }

    double Ix1[k], Ix2[k], Ix3[k];

    // Assign Ix1 to a random value
    for (int i = 0; i < k; i++){
        Ix1[i] = 255 * static_cast<double>(rand()) / RAND_MAX;
        Ix2[i] = 255 * static_cast<double>(rand()) / RAND_MAX;
        Ix3[i] = 255 * static_cast<double>(rand()) / RAND_MAX;
    }
 
    double mean1[k][3];

    for (int i = 0; i < k; i++) {
        mean1[i][0] = Ix1[i];
        mean1[i][1] = Ix2[i];
        mean1[i][2] = Ix3[i];
    }

    int i1 = 1;

    for (i1 = 1; i1 < n; i1++){
        auto Rnk = new int[N1][k];
        auto distance = new float[N1][k];

        for (int i = 0; i < N1; i++) {
            for (int j = 0; j < k; j++) {
                Rnk[i][j] = 0;
            }
        }

        for (int i = 0; i < N1; i++){
            int min_index;
            for (int j = 0; j < k; j++){
                distance[i][j] = (x[i][0] - mean1[j][0])*(x[i][0] - mean1[j][0]) + (x[i][1] - mean1[j][1])*(x[i][1] - mean1[j][1]) + (x[i][2] - mean1[j][2])*(x[i][2] - mean1[j][2]);
            }
            min_index = std::distance(std::begin(distance[i]), std::min_element(std::begin(distance[i]), std::end(distance[i])));
            Rnk[i][min_index] = 1;
        }

        int J1[N1];
        for (int i = 0; i < N1; i++) {
            J1[i] = 0;
        }
        int sumRnk[k]; // Initialize sumRnk array with zeros
            for (int j = 0; j < k; j++) {
            sumRnk[j] = 0;
        }
        
        for (int i = 0; i < N1; i++) {
            for (int j = 0; j < k; j++) {
                J1[i1] = J1[i1] + Rnk[i][j] * distance[i][j];
            }

        for (int j = 0; j < k; j++) {
                sumRnk[j] = sumRnk[j] + Rnk[i][j];
            }
        }
        for (int i = 0; i < N1; i++) {
            int temp[3];
            for (int j = 0; j < k; j++) {
                for (int z = 0; z < 3; z++) {
                    temp[z] = Rnk[i][j] * x[i][z];
                }
                bool allZero = true;
                for (int z = 0; z < 3; z++) {
                    if (temp[z] != 0) {
                        allZero = false;
                        break;
                    }
                }
                if (allZero) {;
                }
                else{
                    for (int z = 0; z < 3; z++) {
                        mean1[j][z] = mean1[j][z] + temp[z];
                    }
                }
            }
        }
        for (int j = 0; j < k; j++) {
            if (sumRnk[j] != 0) {
                for (int z = 0; z < 3; z++) {
                    mean1[j][z] = mean1[j][z] / sumRnk[j];
                }
            }
        }
        if (abs(J1[i1] - J1[i1 - 1]) < n1) {
            break;
        }
        auto x_scatter = new int[N1][3];

        for (int i = 0; i < N1; i++) {
            for (int j = 0; j < 3; j++) {
                x_scatter[i][j] = x[i][j];
            }
        }

        for (int i=0; i < cols; i++) {
            std::cout << x_scatter[i][0] << std::endl;
        }

        // for (int i = 0; i < N1; i++) {
        //     for (int j=0; j < 3; j++) {
        //         std::cout << x_scatter[i][j] << std::endl;
        //     }
        // }

        // Create a new image from x1, x2, and x3 arrays
        cv::Mat x_scatter_image(rows, cols, CV_8UC3);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < x_scatter_image.cols; j++) {
                cv::Vec3b& pixel = x_scatter_image.at<cv::Vec3b>(i, j);
                pixel[0] = x_scatter[i][0];
                pixel[1] = x_scatter[i][1];
                pixel[2] = x_scatter[i][2];
            }
        }

        // // Create a new image from x1, x2, and x3 arrays
        // cv::Mat newImage(rows, cols, CV_8UC3);
        // index = 0;
        // for (int i = 0; i < newImage.rows; i++) {
        //     for (int j = 0; j < newImage.cols; j++) {
        //         cv::Vec3b& pixel = newImage.at<cv::Vec3b>(i, j);
        //         pixel[0] = x[i][0];
        //         pixel[1] = x[i][1];
        //         pixel[2] = x[i][2];
        //     }
        // }

        std::cout << "Iteration: " << i1 << std::endl;
        cv::imshow("x_scatter Image" + std::to_string(i1), x_scatter_image);
        cv::waitKey(0);

        if (abs(J1[i1] - J1[i1 - 1]) < n1){
            break;
        }

        // // Create a new image from x1, x2, and x3 arrays
        // cv::Mat newImage(rows, cols, CV_8UC3);
        // index = 0;
        // for (int i = 0; i < newImage.rows; i++) {
        //     for (int j = 0; j < newImage.cols; j++) {
        //         cv::Vec3b& pixel = newImage.at<cv::Vec3b>(i, j);
        //         pixel[0] = x1[index];
        //         pixel[1] = x2[index];
        //         pixel[2] = x3[index];
        //         index++;
        //     }
        // }
        // cv::imshow("New Image" + std::to_string(i1), newImage);
        // cv::waitKey(0);
    }

    // std::ofstream outputFile("sumRnk.csv");
    // if (outputFile.is_open()){
    //     for (int j = 0; j < 1; j++){
    //         for (int i = 0; i < number_of_pixels; i++){
    //             outputFile << x_scatter[i][j] << ",";
    //             outputFile << x_scatter[i][j+1] << ",";
    //             outputFile << x_scatter[i][j+2] << ", \n";
    //         }
    //     outputFile.close();
    //     }
    //     std::cout << "sumRnk has been stored in sumRnk.csv" << std::endl;
    // } 
    // else{
    //     std::cout << "Failed to open sumRnk.csv" << std::endl;
    // }
    // std::ofstream outputFile2("mean1.csv");
    // if (outputFile2.is_open()){
    //     for (int j = 0; j < 1; j++){
    //         for (int i = 0; i < k; i++){
    //             outputFile2 << mean1[i][0] << ",";
    //             outputFile2 << mean1[i][1] << ",";
    //             outputFile2 << mean1[i][2] << ", \n";
    //         }
    //     }
    //     outputFile2.close();
    //     std::cout << "mean1 has been stored in mean1.csv" << std::endl;
    // }
    // else{
    //     std::cout << "Failed to open mean1.csv" << std::endl;
    // }
    return 0;
}