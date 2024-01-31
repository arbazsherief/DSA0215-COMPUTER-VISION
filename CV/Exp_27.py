import cv2

main_image = cv2.imread("C:\\Users\\arbaz\\OneDrive\\Pictures\\Batman logo.jpg")

if main_image is not None:
    main_height, main_width, _ = main_image.shape
    crop_height, crop_width = 80, 288

    cropped_region = main_image[0:crop_height, 0:crop_width]

    paste_image = cv2.imread("C:\\Users\\arbaz\\OneDrive\\Pictures\\th.jpg")

    if paste_image is not None:
        paste_height, paste_width, _ = paste_image.shape

        # Ensure that the dimensions of cropped_region match the dimensions of the paste region
        cropped_region = cv2.resize(cropped_region, (paste_width, paste_height))

        paste_x, paste_y = main_width - paste_width, main_height - paste_height

        main_image[paste_y:main_height, paste_x:main_width] = cropped_region

        cv2.imshow("Result", main_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
