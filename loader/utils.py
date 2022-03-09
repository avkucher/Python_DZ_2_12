from exceptions import PictureWrongTypeError, PictureUploadError


def save_uploaded_picture(picture):

    filename = picture.filename

    file_type = filename.split('.')[-1]

    if file_type not in ['jpeg', 'jpg', 'png', 'svg']:
        raise PictureWrongTypeError

    picture.save(f'./uploads/images/{filename}')


    return f'uploads/images/{filename}'