#include <iostream>
#include <opencv2/opencv.hpp>
#include <ctime>
#include <dirent.h>
#include <sys/stat.h>

//  g++ -std=c++11 main.cpp -o main -I"c:/opencv/build/include" -L"C:/opencv/build/x64/vc15/lib" -lopencv_core -lopencv_highgui -lopencv_imgcodecs

using namespace std;
using namespace cv;

int main() {
    cout << "Hello !!!" << endl;

    VideoCapture cap("/home/probook/Downloads/Data.mp4");
    int frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
    int frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);
    double fps = cap.get(CAP_PROP_FPS);
    cout << "frame : " << frame_width << " x " << frame_height << ", FPS=" << fps << endl;

    double* ms = new double[(int)fps];
    for (int x = 0; x < fps; x++) {
        ms[x] = (1.0 * x) / fps;
    }
    int second = 0;
    int minute = 0;
    int hr = 0;
    cout << second << endl;
    cout << minute << endl;

    time_t checkpoint = time(nullptr);
    int checkpoint_frame = 0;

    int cnt = 0;
    int cnt2 = 0;
    while (true) {
        if (time(nullptr) - checkpoint >= 1) {
            checkpoint = time(nullptr);
            cout << "FPS : " << cnt2 - checkpoint_frame << endl;
            cnt2 = 0;
        }

        Mat frame;
        bool ret = cap.read(frame);
        if (!ret || frame.empty()) {
            break;
        }

        cnt = (cnt + 1) % (int)fps;
        cnt2++;
        if (cnt == 0) {
            second++;
            char t[10];
            sprintf(t, "%d:%02d:%02d", hr, minute, second);
            string path = "/home/probook/ws_python/vdo2images/img/" + to_string(hr) + '/';
            if (opendir(path.c_str()) == nullptr) {
                mkdir(path.c_str(), S_IRWXU | S_IRWXG | S_IRWXO);
            }
            imwrite(path + t + ".jpg", frame);
            if (second == 60) {               
				second = 0;
				minute++;
				cout << hr << ":" << minute << endl;
			}
			if (minute == 60) {
				minute = 0;
				hr++;
			}
		}

        if (waitKey(1) != -1) {
            break;
        }
    }
}
