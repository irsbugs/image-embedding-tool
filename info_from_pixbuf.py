#!/usr/bin/env python3
#!
# info_from_pixbuf.py
#
# The program decodes a Base64 image. It uses GdkPixbuf.PixbufLoader() to
# load the image into a pixbuf. 
# The details of the information in the pixbuf are then output to the console.
#
# With these details, then, potentially, a GdkPixbuf.Pixbuf.new_from_bytes()
# could be used to used to create the pixbuf.

import gi
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf, GLib
import base64


def get_info(pixbuf):

    #print(dir(pixbuf))

    print("Width:", GdkPixbuf.Pixbuf.get_width(pixbuf))
    print("Heigh:", GdkPixbuf.Pixbuf.get_height(pixbuf))  

    print("Colorspace:", GdkPixbuf.Pixbuf.get_colorspace(pixbuf))  

    print("Byte Length:", GdkPixbuf.Pixbuf.get_byte_length(pixbuf))
    print("Has Alpha?:", GdkPixbuf.Pixbuf.get_has_alpha(pixbuf))
    print("Bits per Sample:", GdkPixbuf.Pixbuf.get_bits_per_sample(pixbuf))

    print("N Channels:", GdkPixbuf.Pixbuf.get_n_channels(pixbuf))
    print("Row stride", GdkPixbuf.Pixbuf.get_rowstride(pixbuf))


    #print("Properties:", GdkPixbuf.Pixbuf.get_properties(pixbuf))
    # TypeError: requires at least one argument

    #print("Pixels:", GdkPixbuf.Pixbuf.get_pixels(pixbuf))
    # Pixels: b'\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff\xff\x00\xff\xff

    #print("Get Options:", GdkPixbuf.Pixbuf.get_options(pixbuf))
    options_dict = GdkPixbuf.Pixbuf.get_options(pixbuf)
    #print(options_dict)
    for key, value in options_dict.items():
        print(key) #, value)
        pass

    print("Get Option ~ original-width:", GdkPixbuf.Pixbuf.get_option(pixbuf, "original-width"))
    print("Get Option ~ original-height:", GdkPixbuf.Pixbuf.get_option(pixbuf, "original-height"))
    print("Get Option ~ x-dpi:", GdkPixbuf.Pixbuf.get_option(pixbuf, "x-dpi"))
    print("Get Option ~ y-dpi:", GdkPixbuf.Pixbuf.get_option(pixbuf, "y-dpi"))
    #print("Get Option ~ icc-profile:", GdkPixbuf.Pixbuf.get_option(pixbuf, "icc-profile"))

    # print("Get Option ~ tEXt:", GdkPixbuf.Pixbuf.get_option(pixbuf, "tEXt::Raw profile type exif"))
    # 'tEXt::Raw profile type exif': '\nexif\n    3716\n45786966000049492a00...



    print("\nRetrieve the supported formats...")
    pixbuf_format = GdkPixbuf.Pixbuf.get_formats()
    for item in pixbuf_format:
        mime_list = GdkPixbuf.PixbufFormat.get_mime_types(item)
        for mime in mime_list:
            print(mime)
        description = GdkPixbuf.PixbufFormat.get_description(item)
        print(description)
        extension = GdkPixbuf.PixbufFormat.get_extensions(item)
        print(extension)
        lincese = GdkPixbuf.PixbufFormat.get_license(item)    
        print(license)
        name = GdkPixbuf.PixbufFormat.get_name(item)     
        print(name)
        is_disabled = GdkPixbuf.PixbufFormat.is_disabled(item)    
        print(is_disabled)
        is_scalable = GdkPixbuf.PixbufFormat.is_scalable(item)
        print(is_scalable)
        is_writable = GdkPixbuf.PixbufFormat.is_writable(item)
        print(is_writable)
        print()
      	
  	
def get_image_from_base64(B64_IMAGE):   
    # Decode base64 data
    image_data = base64.decodebytes(B64_IMAGE)
   
    # Use PixbufLoader to load the image_data to Pixbuf data.
    loader = GdkPixbuf.PixbufLoader()        
    loader.write(image_data)
    loader.close()
    pixbuf = loader.get_pixbuf()                
    return pixbuf 
    
B64_IMAGE = (b"""
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
""")


B64_IMAGE_1 = (b"""
PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+Cjwh
LS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoK
PHN2ZwogICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgIHht
bG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOnJkZj0iaHR0
cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgeG1sbnM6c3ZnPSJo
dHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIw
MDAvc3ZnIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5l
dC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3Nj
YXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB3aWR0aD0iMzIiCiAgIGhlaWdodD0iMzIi
CiAgIGlkPSJzdmcyOTkxIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlua3NjYXBlOnZlcnNpb249IjAu
OTIuNSAoMjA2MGVjMWY5ZiwgMjAyMC0wNC0wOCkiCiAgIGlua3NjYXBlOmV4cG9ydC14ZHBpPSI5
MCIKICAgaW5rc2NhcGU6ZXhwb3J0LXlkcGk9IjkwIgogICBzb2RpcG9kaTpkb2NuYW1lPSJmYXZp
Y29uX2JsdWVfMzJfYmlnLnN2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczI5OTMiIC8+CiAgPHNv
ZGlwb2RpOm5hbWVkdmlldwogICAgIGlkPSJiYXNlIgogICAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIK
ICAgICBib3JkZXJjb2xvcj0iIzY2NjY2NiIKICAgICBib3JkZXJvcGFjaXR5PSIxLjAiCiAgICAg
aW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgog
ICAgIGlua3NjYXBlOnpvb209IjIyLjYyNzQxNyIKICAgICBpbmtzY2FwZTpjeD0iMTUuMDIzMTY5
IgogICAgIGlua3NjYXBlOmN5PSIxNi41MjA5NzgiCiAgICAgaW5rc2NhcGU6ZG9jdW1lbnQtdW5p
dHM9InB4IgogICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9ImxheWVyMSIKICAgICBzaG93Z3Jp
ZD0idHJ1ZSIKICAgICBib3JkZXJsYXllcj0idHJ1ZSIKICAgICBvYmplY3R0b2xlcmFuY2U9IjEi
CiAgICAgZ3JpZHRvbGVyYW5jZT0iMSIKICAgICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjEzNTUi
CiAgICAgaW5rc2NhcGU6d2luZG93LWhlaWdodD0iMTAwMiIKICAgICBpbmtzY2FwZTp3aW5kb3ct
eD0iMTUxIgogICAgIGlua3NjYXBlOndpbmRvdy15PSI0MiIKICAgICBpbmtzY2FwZTp3aW5kb3ct
bWF4aW1pemVkPSIwIgogICAgIHNob3dndWlkZXM9ImZhbHNlIj4KICAgIDxpbmtzY2FwZTpncmlk
CiAgICAgICB0eXBlPSJ4eWdyaWQiCiAgICAgICBpZD0iZ3JpZDMxMjEiCiAgICAgICBlbXBzcGFj
aW5nPSI1IgogICAgICAgdmlzaWJsZT0idHJ1ZSIKICAgICAgIGVuYWJsZWQ9InRydWUiCiAgICAg
ICBzbmFwdmlzaWJsZWdyaWRsaW5lc29ubHk9ImZhbHNlIiAvPgogIDwvc29kaXBvZGk6bmFtZWR2
aWV3PgogIDxtZXRhZGF0YQogICAgIGlkPSJtZXRhZGF0YTI5OTYiPgogICAgPHJkZjpSREY+CiAg
ICAgIDxjYzpXb3JrCiAgICAgICAgIHJkZjphYm91dD0iIj4KICAgICAgICA8ZGM6Zm9ybWF0Pmlt
YWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgIHJkZjpy
ZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiIC8+CiAgICAg
ICAgPGRjOnRpdGxlPjwvZGM6dGl0bGU+CiAgICAgIDwvY2M6V29yaz4KICAgIDwvcmRmOlJERj4K
ICA8L21ldGFkYXRhPgogIDxnCiAgICAgaW5rc2NhcGU6bGFiZWw9IkxheWVyIDEiCiAgICAgaW5r
c2NhcGU6Z3JvdXBtb2RlPSJsYXllciIKICAgICBpZD0ibGF5ZXIxIgogICAgIHRyYW5zZm9ybT0i
dHJhbnNsYXRlKDAsLTEwMjAuMzYyMikiPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiNm
NWFiMTQ7ZmlsbC1vcGFjaXR5OjE7ZmlsbC1ydWxlOm5vbnplcm87c3Ryb2tlOm5vbmU7c3Ryb2tl
LXdpZHRoOjIuMzMzMzMzMjUiCiAgICAgICBkPSJtIDIzLjQzNzUsMTAyMi4zNjIyIHYgMTguODEy
NSBsIC01LjEwNDE2NywtNi41Nzg0IGMgMC4wMTY1NywxMC4zMDA4IDAsLTAuNDk3NyAtMC4wMjMx
LDkuODM3NCBsIDQuNjE2ODI3LDUuOTI4NSBIIDMwIHYgLTI4IHoiCiAgICAgICBpZD0icGF0aDI4
LTUiCiAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgc29kaXBv
ZGk6bm9kZXR5cGVzPSJjY2NjY2NjYyIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDoj
MzNhNGQ1O2ZpbGwtb3BhY2l0eToxO2ZpbGwtcnVsZTpub256ZXJvO3N0cm9rZTpub25lO3N0cm9r
ZS13aWR0aDoyLjMzMzMzMzI1IgogICAgICAgZD0ibSAxLjk5OTk5OTgsMTAyMi4zNjIyIHYgMjgg
aCA2LjU2MjQ5OTkgdiAtMTguNDQ4IGwgNy4zOTg4MzAzLDkuNTY1NyBjIDAsMCAwLjAxMTA4LC0w
LjE0OTMgMC4wMzg2OCwtOS45MjYyIGwgLTcuMTQ1ODMzLC05LjE5MTUgeiIKICAgICAgIGlkPSJw
YXRoMjgiCiAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgc29k
aXBvZGk6bm9kZXR5cGVzPSJjY2NjY2NjYyIgLz4KICA8L2c+Cjwvc3ZnPgo=
""")

B64_IMAGE_2 = (b"""
AAABAAEAMjIAAAEAGABoHwAAFgAAACgAAAAyAAAAZAAAAAEAGAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAD/////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////8AAP//////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////wAA////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////AAD/////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////8AAP//////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////wAA////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////AAD/////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////8AAP//////////////////
//////////////////////////////////////7+/v39/f///////+bm5re3t5WVlYGBgW9vb25t
bW5tbW5ubmxra29vb4qKipycnMvLy/Pz8/////r6+vv8/Pj4+P////7+/vn5+f39/fz8/P39/f//
//////////////7+/v7+/v7+/v7+/gAA////////////////////////////////////////////
/v7+//3++/7/////3ODfcW9vFA4OAAAAAAAAAAMFCA4REhwgFyMlGyorGSsrDyEhERseBgkMAAAA
AAAAAAAALSwsm5WV//f4/////Pz7/P39/f7+/f39/////////////////v7+////////////////
////AAD////////////////////////////////////////////8/v75/Pz59/dGRUcAAAAACQg+
WVdxmpiNvbmXz8ya09Cc1NGX1tSS1NKW1tSb1dSh0tOm0NGbyMSNtK9sh4QyPTwAAAAEAgOIiIf/
///9/f3////////////////////////////////////+/v7+/v7+/v4AAP//////////////////
//////////////////////////r+/s/X1QwODSAkJXeTlJzX1ofTz3/NyYPOyYfMx5PQyqDY0ou2
tnegoom0tqPY14zNzIPPy4zPy4/Py5DLyaLW1pfJyFV5eQAAAEFGRvz7+//+//////7/////////
//////////////7+/v7+/v///////wAA/////////////////////////////////f39/v7+/f39
9fT0BAYFUWhkp9jWj87Nis7Pi8vNlc7QmsnLpcrLVGZmAAQDAAAAAAAAAAAAAgoMV35/l9XTiMzM
hsrKiMvMiMvLi83NjcvKpdDMHSoqUVBS/////v7+/f//////////////////////////////////
////AAD////////////////////////////////////6+vr///8uLS5hdXeb0s9/0cx/z8yQy82O
y8uNy8t7r7AgOjxScHOHqquSzMuc1dSk09OPtbhTa25IaWyQz9CMzM2MzM2MzM2LzM2Nzs6Py8uq
1tQWIyOUmJj9/Pz///////////////////////////////////////8AAP//////////////////
//////////////7+/v///42MjB4wMJzU1pHP0IfLyYnNy47NzIzNyozMyJLNy5fS0o3MzYvMzY3L
yozOzIjOy4fNyo7MypjPzorKyYvLyovLyozNzIzMy4vNy4bMypHOzZjDwAAAAOzt7P78/P//////
/////////////////////////////wAA/////////////////////v/++P39+/z8/v7+zdTUAAAA
m8XBidHMicrMjc3Ri8nNkc3QiMnGot/biL26h7e3iL69ndnYmNPPhMvGic/KnNfWm9TUgLm6h7Sv
nM/KndjTjczJi8rHj83Mjc3NjcvLj8PCeZeVGBcZ////+vz5/P78+vv7///+///+////////////
////AAD////////////////////+///5/f39/Pzo5ecKDQ2VsrBilJCLzsyIzM2Jys6Rys6e0dJr
h4kHDhEGCQsZHyIUFxoAAAQ3R0eNq6tuiYodJygAAwkXGx4ZIyMAAAAiMjKKtLOR09B+zsmMzMyM
zcua1NNUfHxtgIJBQEH////6+vn//v3///7///7///7///////////8AAP//////////////////
//////n6+vXy8yMfIXyJizReXJzU1I3Ky43Nz4vJyqHS1CY7PRwyM4K0taLb2prY1pvV1KHW1m2O
jggOER8xMoqws7HT16nV2JfZ1KjW1HGLjAAFCGeFhp7Q0I3NzIrOy4rNyZfMyTNJSVdlZmBdXf//
/////////vv//v3//////////////wAA/////////////Pz8/v7+//7/8/PyDg4OAAAAT2lrm9LS
jsvMhLu+lczNn9PSGTIxZIKBo87PksnKi87Nhc7Mis3MkMzMlNLNNERFZJSShM3Jjs3Mf8/Mhc7K
hM/LiM3KoNTUIjI1dYSGl8zKmNbReLu3kc3MntHREiEiAAACVVFU/////Pv6+f79+/7+////////
////AAD////////////9/f3///////8xLy4AAABYd3aazs6QzM6V0NI5ZGSItLRDX15ihIOf0tGR
zM2OzMyNzMyMzcyNzcyOzMyP0s04P0Jtjo+JzsuZysyIzcydyc2PzMyAz8uF0c2b1tQYMTCYtrZJ
cG1koJ2LzMqQzMyg0dIeKiwAAAOXlJX////6/Pr7/vz///////////8AAP////////////7+/v39
/bu5uQAAAEVdWp3X04zRz4vKzI/Ky6LY1C1APQsREKHMzZLV1oTS0obOzY3NzZLKzY/LzIrNzYTU
zTc/QmqOj4PPypzKzIfNzInMzYzMzZDLzJXKyara2X2lpAAAAGqGhZzQz4vMy4rMy5DOzaPQ0Q4V
FwgFCP/8/Pz9/P///////////////wAA/////////////f39////U1NTCxQUmtbSjczMhs7Mhc7M
kc3LjMvKodHTeaGkNUlNT3Z6ncvQhsvLes3Li8zMo9PVldDPjtLQNkJIZ4+TgMzKmNPUks/OiszM
hMvNi87Qjb7BL1NTRl1dlcTKls3PjszNis3Nh83MhMzKi8/Mhq6tAAAAvbm6/Pz8+v79////////
////AAD////////////+/v7///8VFBRlgH+JysWTzs+JzcyGz8uRz8uEyceQzcyOyMiT0M+N0c+N
zcyZ0dGhz9CTvbwsP0BEXV2c19IzRklti4uMvr0pPD1SZ2eT1dGg0dOZyMyPzc6S09GPzMqMzc2I
yMmKysqMy8uSz8+MzcuLzcqj1dMXJSWPjo/9+/v+//7///////////8AAP////////////7+/v//
/xMSEoWwq4fQyJLKzI/LzI7PzaDRz3iqqXenp6LX1IzNyYLQyovY0DdXVUBFSQcLCw0cHBERERkr
JxskJD1FRAULChIZGRgVFgcZFjA6O3mhpX3My4LOy6DU1JLExHSkpYW0tabY2ZDIyY/NzIzNzJbS
zT1RUIeNjP////7+/f///////////wAA/////////////v7+////OTc4gqqmg83Gj8rLkc3NYZmY
WGtsAAAAQUBCAAECS2hmpNHNkdDKfqSjCwYIHxocGBkZIRUXHBMTCwgHEgsKGRcWFBwZHBoZKhse
BwwOm9LRg8/NkcDBKTAzICAgHxscGR0gUHN0e7Szjc7Ni8vKmdTQNUhHo6in//////7+////////
////AAD////////////6+vr///+CgoJjfnyGz8iKzs2PzMyn09QcIiXEwML///////9pa2sfJyee
yMWi0M4zREYVFxkfGR0QDQ4OAAAMDg0XERIJAAELFxUbGxoNBgl4nJyWzs2EpqkGCQqwra//////
//9dWVxid3mh1dWJzcqHyseq29kMGhnf4eH//Pz+//7///////////8AAP////////////////7+
/trX1x0qK5LY0oPLyo/Qz1RydbCxtPb7+//+/f////n9+8nPzhYkI43Bvp/S0yo8QBURFhYaHB0Y
GAUQDhsdHCYYGxcdHQkFBmSJiZTU0mCFhD03POnk54GIiWtxb72/u////z9HS5rFx4vMy4rPzZnD
wQsOD////////////////////////wAA/v7+/f399fX1Ozs7mpqa////FBQVjsbDjsvLl9XTHS0t
////+v3/wsPDGRwYABowABg9FRskAwsNcZKWpNTWPFxhBAIACAUFAQMGAgABEAcKAAIBep+bpN3b
OEpMi4SAkpydAA0fH1mjI2i3EjpZREVS29zhP1lXjM/SjMvKa3+CdnN1////XV5ea2tr/////f39
////AAD+/v7///97e3sAAAAAAACTk5Oam55RZ2ePzsyHvrxsdnj//fu5wbcAAiYueOMolf8jj/oq
hfMcMVw9PTUzSkemzs6FrLNajoyd19KHwLtdjIio2dV2paIjJy/LwbfO1dwBETYmi+kUj+kWhPMS
iPkeV7KJhIgmPSqX19ui2NkKExT///8uLCwFBgYAAADl5eX6+vr///8AAP///////xUVFQUFBQEB
ARESEuPl5RsaHZnS0oOzsYeLjP///yYhJzKF3xGB2wUhTBQpWRl/4h2J8Sc2SoaJgh0jIzZCTG6U
lX+jon6hoGB+fR0pKhIVF8vQ1f//+T5DTSdtwiB85QEIKQIADhldoBSU+ilCVzdCRZ3U4mWKimRp
aLOwsAAAAAMCAwMCA3Fxcf7+/v///wAA/v7+0NDQAAAAAAAAAAAAAAAAJCQkCgMHSWdnlsXDanBw
//75ARQzFon/DDZiDwcAAAEBDDZjBX3/EDd1V2BYwubngKqoJSYnCAABAAAARmNljL+/hq2wgZeQ
////NSo1Gn7iGUyQBAMAHiEhDB43Boz5MVyJN0JAreLcEh8eAAAAMC4tAgQCAwEDAQABFRUV////
////AAD///9JSUkAAAAAAAAAAAAAAAAYGhkEAAESHyCp3dgpPTn///8BFisajP4cS5IuLizl/f9i
gaAdgf8VQHI1TEeV1diKy8RwnpsAAAACCgys2dqNysun1NlOPT3///9JR0cZfMoVfdcODxn///+m
uMIdgPcZPnNWh49upqYDBgUHBAMUEhABAwEEAQQBAAEAAAC4uLj8/PwAANvb2wAAAAICAgAAAAAA
AAAAAAEBAAIBAj5KTI3FwH+ppaakpVJQViVwwReG8h8/drvAxjxznDCO7AEMG2mOj4fHy5LNyqPQ
zgAAADI7PpvPz4fQz4/U1CEwMbq9u8HIxQ4vYRyB9yJuu2hzmyhpizqT9QsaKaTWyKrIwwAAAAYE
AwIAAAABAAEAAQMCAwMDAyMjI////wAAbW1tAQEBAQEBAAAAAAAAAAEAAgEABAAAKDk4mNXQlczM
XHVwoKecNDlCJliSKovkHnvCN4bTEi1eAQgJptLOgs3Ois7KnNnTFBwfTmFjjs7Mjs7NjMvLdp6a
AAAAz8nHfoKODzdtInrWOJfnOnrHECRMjLzCj87Jms3LAAAAAAAAAwAAAQAAAAEAAQICAAAAAAAA
wsLCAAATExMDAwMCAgIAAAAAAAAAAAABAQACAAAUIB+h29aU0tA/YWx6kJ5kaWJWWVsaIDYIBR0G
ABEAAAd4qJeEzcSEy9KVyc6X1dAiLjBdenqLzcuOzs2LzMua1NkvSE0AAABOTEmMkpk0OVEVFSZD
VGVsl59ahYWMysuAtbcAAAABAgEDAAABAAAAAQABAQEBAQEEBARycnIAABcXFwMDAwEBAQAAAAAA
AAAAAAEBAAIBAQAAAKbW1IvLyZHHvgADABcfGQ8WHwAACQAFAAMCAniVj5PXy4bMzJDJ0o/My5PW
0CQyNF58fYzNy47NzIvLy4zNzqLS2zlQUwAAAAQAABAGAx4iGgsMCCw6N6DX1IXLylJ8fAAAAAAB
AAIBAQEAAAAAAAEBAQUFBQEBAXV1dQAAs7OzAAAAAwMDAAAAAAAAAAAAAQEAAgAAAAAAa4yLkM3L
iM3Oi77CR09VHRcZIiUjTWhfkMPBkM7RhcnOkcnSlMrNic/JmtrTGCAhVGtsjM3LjczMjs3NjMzH
kczQms/TfaWhNUlICxIXHycqUHpzjM3Jj8rMptPRKT85AAEBAAAAAAAAAAAAAAAAAQEBAwMDFRUV
6urqAAD////AwMACAgIAAAAAAAAAAAAAAQABAAADAAMdKSue0dKFzciL0c+I0NWZ292a19SS0M+G
zcqKzc+PytCKzMuKzsqOy8ybzcwAAAEoODuU09GNzMyJzMuRzsuLys2Lz82JzcSX0tCj2eKY2dyb
y8aTzs+CydCXxMMAAAADAAAAAAABAQEAAAAAAAABAQEiIiL19fX8/PwAAPz8/P///8zMzAAAAAIC
AgEBAQACAQEAAAQBAgAAAGWFgqPT0pLGypDMzI7NyY7Oy4jK0I/NzZPMyI3KyYrTzIbNypbN0Uxn
ZQQAAQAAAJW7vJHKyoTNy5PLzI/KzIzOy4zRyYvMyJDMzo7MzYPOx4TRzpvS1SAtLgQFBAEAAAEB
AQEBAQICAgMDAx0dHf////z8/P39/QAA/////f39////urq6AAAABQUFAQIBAwICAgAAAQMCAAIB
YISBmtvZjcvLjtDQjNHPg83Lic/Mic7LidDNisvJm8/Pc5udAAEABQMCAgECEBgaoc3PisrJjs7O
is7MiM3Mis7NicnJlNLSlc3Ol87OptTSKD49AAIABgQEAAEBAQEBBAQEBAQEGxsb8vLy/Pz8/f39
////AAD9/f3////+/v78/Pza2tpMTEwAAAAAAAACAAACAAAAAgEAAAAZIiM6Tk42W1uMxMWWy86D
yMiF0M6Lzcqg09FVb20AAAAAAwIGBAUFAAEBAwYEDA9+oKOb29iGy8eJ0MyK0MyM0MxspqQqR0o1
SEoDCg0DAgMEAAAEAQEAAAAAAAANDQ10dHT6+vr6+vr////9/f3+/v4AAP7+/v////7+/v7+/v7+
/v///////+fn55qWl0VBQgAAAAYCAiMjIpi4tKTa1o7Ny4/KzKrZ3I20t01nZwAEAwACAAYEAgIE
AwMCAggDBAgDBQMDBQAAAA0cHWiGhp/MypzTz5HOyZfQzLrb2niKjAUFBwQAAggGCFxeX7m5ufX1
9f////////39/f7+/v39/f///////wAA/////////////////////////v7+/f39////////4+Li
VVJSAQIAAAAARFlYX4WDSWdmEhsfAAAADxETISIjNTU0QkNBTU1OT05OT09PSkhIQj4/My8wJRse
CgYIAAAALDs6VndzW3x4LTc3AAAAExQVhoaG/v///f///f39/v7+/v7+////////////////////
+vr6AAD////////////////////////9/f3+///6/Pz6/f36/v3////39fepo6RdWllXU1SZl5jX
29n4+fj////////////////////////////////////////////+/f/y9fW+wsOAfn5TTU5zc3PD
xsX////+/////f/+/f79/f3////////////////+/v7////+/v7+/v4AAP//////////////////
//////////////////7///7///7///z+/v39/f///////////vz+/f7///7//v////7/////////
//////7///7///7///////7///z9/f7////////////////////+/v////7+///+//79/f//////
//////7+/v////////7+/v7+/v7+/gAA////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////AAD/////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////8AAP//////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////wAA////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////AAD/////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////8AAP//////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
""")

if __name__=="__main__":
    # Change the commenting to select the B64_IMAGE.
    pixbuf = get_image_from_base64(B64_IMAGE)
    #pixbuf = get_image_from_base64(B64_IMAGE_1)
    #pixbuf = get_image_from_base64(B64_IMAGE_2)    
    
    get_info(pixbuf)


