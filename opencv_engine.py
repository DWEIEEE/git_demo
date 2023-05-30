import cv2
# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
class opencv_engine(object):

    @staticmethod
    def point_float_to_int(point):
        return (int(point[0]), int(point[1]))

    @staticmethod
    def read_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def draw_point(img, point=(0, 0), color = (0, 0, 255)): # red
        point = opencv_engine.point_float_to_int(point)
        print(f"get {point=}")
        point_size = 1
        thickness = 4
        return cv2.circle(img, point, point_size, color, thickness)

    @staticmethod
    def getvideoinfo(video_path): 
        # https://docs.opencv.org/4.5.3/dc/d3d/videoio_8hpp.html
        videoinfo = {}
        vc = cv2.VideoCapture(video_path)
        videoinfo["vc"] = vc
        videoinfo["fps"] = vc.get(cv2.CAP_PROP_FPS)
        videoinfo["frame_count"] = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
        videoinfo["width"] = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
        videoinfo["height"] = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return videoinfo