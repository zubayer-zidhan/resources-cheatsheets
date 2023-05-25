import win32com.client
import os
import datetime




# print(os.getcwd())

curr_directory = os.getcwd()

# numbers = [190710007001, 190710007002, 190710007003]


# roll numbers
rolls = [n for n in range(190710007001, 190710007060)]
extra_rolls = [n for n in range(200750007001, 200750007008)]
rolls.extend(extra_rolls)
rolls.remove(190710007020)
rolls.remove(190710007027)
rolls.remove(190710007033)
rolls.remove(200750007004)
# print(rolls)
# print(len(rolls))


# ***************** CODE STARTS ********************
# Define the path to the Illustrator document and the new name and image
document_path = os.path.join(curr_directory, "farewell_invitation.ai")


# Create an instance of the Illustrator application
app = win32com.client.Dispatch('Illustrator.Application')


# Open the document
document = app.Open(document_path)


starting_time = datetime.datetime.now()
print("Started at: ", starting_time)


# Get the desired text box by comparing properties
target_textbox = None
target_textbox_name = '190710007001'  # Name of the desired text box

for text_frame in document.TextFrames:
    if text_frame.Contents == target_textbox_name:
        target_textbox = text_frame
        break

# Check if the target text box was found
if target_textbox:
    # Perform operations on the target text box
    # print("Target Textbox: ", target_textbox)
    # print('Found the target text box:', target_textbox.Contents)
    # ... do something with the target text box ...
    for number in rolls:
        target_textbox.Contents = str(number)
        # # Set up the export options for JPEG
        # jpeg_export_options = win32com.client.Dispatch('Illustrator.ExportOptionsJPEG')
        # jpeg_export_options.AntiAliasing = True
        # jpeg_export_options.ArtBoardClipping = True
        # jpeg_export_options.QualitySetting = 100
        # jpeg_export_options.HorizontalScale = 100.0
        # jpeg_export_options.VerticalScale = 100.0

        # Export the updated document as a PNG file
        png_export_options = win32com.client.Dispatch('Illustrator.ExportOptionsPNG24')
        png_export_options.Transparency = True
        png_export_options.AntiAliasing = True
        png_export_options.ArtBoardClipping = True
        # png_export_options.SaveAsHTMLCompatible = False
        png_export_options.VerticalScale = 300.0
        png_export_options.HorizontalScale = 300.0
        # png_export_options.matte = False
        # png_export_options.qualitySetting = 100
        # png_export_options.PNG8 = False


        image_name = str(number) + ".png"

        new_images_path = os.path.join(curr_directory, 'exports', image_name)
        print(new_images_path)

        document.Export(
            new_images_path,
            5,
            png_export_options
        )


        # image_name = str(number) + ".jpg"

        # new_images_path = os.path.join(curr_directory, 'exports', image_name)

        # # Export the updated document as a JPEG file
        # document.Export(
        #     new_images_path,
        #     6,
        #     jpeg_export_options
        # )

else:
    print('Target text box not found')

ending_time = datetime.datetime.now()
print("Ends at: ", ending_time)

# Get a reference to the text frame that contains the name
# name_frame = document.TextFrames.Item(1)
 
# print(name_frame.Contents)

# Update the text in the frame with the new name
# name_frame.Contents = new_name


# # Export the updated document as a PNG file
# png_export_options = win32com.client.Dispatch('Illustrator.ExportOptionsPNG24')
# png_export_options.Transparency = True
# png_export_options.AntiAliasing = True
# png_export_options.ArtBoardClipping = True
# png_export_options.SaveAsHTMLCompatible = False
# png_export_options.VerticalScale = 100.0
# png_export_options.HorizontalScale = 100.0
# png_export_options.matte = False
# png_export_options.qualitySetting = 100
# png_export_options.PNG8 = False

# document.Export(
#     'path/to/exported/image.png',
#     win32com.client.constants.aiPNG24,
#     png_export_options
# )





# Close the document
# document.Close()
