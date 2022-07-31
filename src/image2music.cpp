//! [includes]
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

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
    cv::imshow("Display window", img);
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
