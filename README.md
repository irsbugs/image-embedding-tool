# Image Embedding Tool.
 
This tool converts an image to Base 64 text which may then be embedded into a 
python GTK program.

When the program is run the Base 64 text is then be reverted back to an image 
and may be used as the GUI programs logo or favicon, etc.

As well as the base 64 variable, the following need to be added to the GTK 
program that is being developed.

1.  At the start of the program add the following imports:
```
* import tempfile
* import base64
* import os
```

2.  For the image to be used as a favicon and display in the system tray, then
    after the Gtk.Window() class has been created add the line:
 ```       
    self.image_path_file = self.get_image_temp_file_path()
```

3. Add the following function:
```
    def get_image_temp_file_path(self):
        '''
        Select the desired B64_IMAGE data and decode it to binary bytes.
        Create a temp file. Returns tuple, E.g.  (13, '/tmp/icon_em0f7c2r.ico')
        [0] An OS-level handle to an open file as would be returned by os.open() 
        [1] The absolute pathname of the file.
        Write out binary bytes to the temp file.
        Return the file path
        '''
        
        # Select the embedded icon image stored in base64
        if ICON_IMAGE == 0:
            b64_image = B64_IMAGE
        elif ICON_IMAGE == 1:
            b64_image = B64_IMAGE_1
        elif ICON_IMAGE == 2:
            b64_image = B64_IMAGE_2

        # Decode base64 data
        image_data = base64.decodebytes(b64_image)
                
        # Use tempfile to create a /tmp/ file for the image
        temp_file_tuple = tempfile.mkstemp(suffix=".ico", 
                                           prefix="icon_", 
                                           dir=None, 
                                           text=False)

        # Write to image to temp_file
        with open(temp_file_tuple[0], "wb") as fout:
            fout.write(image_data)

        # Return path and temp filename
        return temp_file_tuple[1]    
```

4.  If its desired to use the image as a Logo, then during the setup of the
    GUI include code like this:
```
        image = Gtk.Image.new_from_file(self.image_path_file)

        #os.remove(self.image_path_file)

        vbox.pack_start(image, expand=True, fill=True, padding=0)

        self.add(vbox)            
```


