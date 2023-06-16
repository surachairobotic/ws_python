import cv2

def detect_license_plate(image_path):
    """
    Load an image file, detect all license plate regions of interest (ROIs) using OpenCV that match the aspect ratio condition, and return a list of the ROI images.
    """
    # Load the image file
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filtering to reduce noise while preserving edges
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Detect edges using the Canny algorithm
    edges = cv2.Canny(gray, 30, 200)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize an empty list to store the license plate ROIs
    rois = []

    # Iterate through the contours to find the license plate regions of interest (ROIs)
    for contour in contours:
        # Calculate the perimeter of the contour
        perimeter = cv2.arcLength(contour, True)

        # Approximate the contour with a polygon
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # If the polygon has four vertices (i.e. it's a rectangle)
        if len(approx) == 4:
            # Get the bounding box of the rectangle
            x, y, w, h = cv2.boundingRect(approx)

            # If the bounding box has the aspect ratio of a license plate
            aspect_ratio = w / float(h)
            if 2.5 <= aspect_ratio <= 5.0:
                # Extract the license plate region of interest (ROI) as a new image
                roi = image[y:y+h, x:x+w]

                # Append the ROI to the list
                rois.append(roi)

    # Return the list of license plate ROIs
    return rois

def main():
    rois = detect_license_plate("00001.jpg")
    for roi in rois:
        cv2.imshow("License plate", roi)
        cv2.waitKey(0)	#if roi is not None:
	#	cv2.imshow("License plate", roi)
	#	cv2.waitKey(0)

if __name__ == '__main__':
    main()