//! [includes]
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>
#include <matlab.hpp>

#include <iostream>

using namespace cv;
//! [includes]

int display_image()
{


    //! [imread]
    std::string image_path = samples::findFile("vtx250.jpg");
    Mat img = imread(image_path, IMREAD_COLOR);

    //! [empty]
    if(img.empty())
    {
        std::cout << "Could not read the image" << std::endl;
        return 1;
    }
    //! [empty]

    //! [imshow]
    cv::resize(img, img, cv::Size(img.cols * 1024.0/img.rows , 1024), 0, 0, cv::INTER_LINEAR);

    Mat img_gray;
    cv::cvtColor(img, img_gray, cv::COLOR_BGR2GRAY);

    Mat col_i = img.col(0);
    Mat col_i_gray = img_gray.col(0);
    ifft(col_i_gray);
    std::cout << col_i << std::endl;
    std::cout << col_i_gray << std::endl;

    cv::imshow("Display window", img);
    cv::imshow("Display window gray", img_gray);
    int k = cv::waitKey(0); // Wait for a keystroke in the window
    //! [imshow]

    //! [imsave]
    if(k == 's')
    {
	    cv::imwrite("starry_night.png", img);
    }
    //! [imsave]

    return 0;
}

int main()
{
  display_image();
}
