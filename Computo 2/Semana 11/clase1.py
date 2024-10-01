from PIL import Image

"foto = Image.open(base.jpg).rotate(45)"
"foto_rotada = foto.rotate(45)"
foto = Image.open("base.jpg")
tranpo1 = foto.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

tranpo1.show()