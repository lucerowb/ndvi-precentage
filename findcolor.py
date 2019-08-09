from PIL import Image

def compute_percentage_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1
            total = r_total + g_total + b_total

    return (r_total/total,g_total/total,b_total/total)

img = Image.open('result.jpg')
#img = img.resize((50,50))  # Small optimization
average_color = compute_percentage_image_color(img)
print(" The red percentage is ", average_color[0]*100, "%")
print(" The green percentage is ", average_color[1]*100, "%")
print(" The blue percentage is ", average_color[2]*100, "%")