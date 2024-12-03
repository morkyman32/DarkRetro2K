# Replace the value under the my_color_scheme variable
# and run the Python code on a Python interpeter.
# The output of this code can be replaced with everything
# that is listed under Colorful stuff under the body CSS celector
#
# You can use an online Python IDE/Interpreter:
# https://www.online-python.com/

my_color_scheme='#ff95db'

import colorsys
import matplotlib.colors

def hsv_to_hex(h, s, v):
  r, g, b = colorsys.hsv_to_rgb(h, s, v)
  r_int = int(r * 255)
  g_int = int(g * 255)
  b_int = int(b * 255)
  hex_code = "#%02x%02x%02x" % (r_int, g_int, b_int)
  return hex_code


rgb_vals=matplotlib.colors.to_rgb(my_color_scheme)
hsv_vals=colorsys.rgb_to_hsv(rgb_vals[0],rgb_vals[1],rgb_vals[2])

# Example usage
h = hsv_vals[0]  # Hue (red)
s = hsv_vals[1]  # Saturation
v = hsv_vals[2]  # Value (bright)

print()
print(f"/* Colorful stuff */")
hex_color = hsv_to_hex(h, s, 0.071 ); print(f"--body-background-color: {hex_color};")
hex_color = hsv_to_hex(h, s, 0.25  ); print(f"--notice-info-background: {hex_color};")
hex_color = hsv_to_hex(h, s, 0.59  ); print(f"--notice-info-border-color: {hex_color};")
hex_color = hsv_to_hex(h, s, 0.106 ); print(f"--form-button-background: {hex_color};")
hex_color = hsv_to_hex(h, s, 0.267 ); print(f"--form-button-hover-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.345, 1 ); print(f"--form-button-text-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.257, 0.671 ); print(f"--form-button-border-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.398, 0.71 ); print(f"--form-button-active-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.673, 0.192 ); print(f"--post-artist-commentary-container-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.257, 0.671 ); print(f"--post-artist-commentary-container-border-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.673, 0.192 ); print(f"--post-search-notice-background: {hex_color};")
print(f"--post-notice-border-color: var(--post-artist-commentary-container-border-color);")
hex_color = hsv_to_hex(h, 0.848, 0.310); print(f"--post-pending-notice-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.789, 0.224); print(f"--post-resized-notice-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.482, 1.0); print(f"--link-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.10, 1.0); print(f"--link-hover-color: {hex_color};")
print(f"--post-tooltip-background-color: var(--post-artist-commentary-container-background);")
print(f"--post-tooltip-header-background-color: var(--post-tooltip-background-color);")
print(f"--post-tooltip-border-color: var(--notice-info-border-color);")
hex_color = hsv_to_hex(h, 0.268, 0.498); print(f"--box-shadow-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.595, 0.514); print(f"--subnav-menu-border-b: {hex_color};")
hex_color = hsv_to_hex(h, 1.0, 0.835); print(f"--subnav-menu-border-t: {hex_color};")
hex_color = hsv_to_hex(h, 0.694, 0.192); print(f"--subnav-menu-grad-b: {hex_color};")
hex_color = hsv_to_hex(h, 1.0, 0.357); print(f"--subnav-menu-grad-t: {hex_color};")
hex_color = hsv_to_hex(h, 0.833, 0.047); print(f"--textbox-grad-b: {hex_color};")
hex_color = hsv_to_hex(h, 0.698, 0.169); print(f"--textbox-grad-t: {hex_color};")
hex_color = hsv_to_hex(h, 0.772, 0.158); print(f"--chip-primary-background-color: {hex_color};")
hex_color = hsv_to_hex(h, 0.667, 0.388); print(f"--default-border-color: {hex_color};")
hex_color = hsv_to_hex(h, 0, 0); print(f"--autosuggestions-box-background: {hex_color};")
hex_color = hsv_to_hex(h, 0.694, 0.192); print(f"--responsive-menu-background-color: {hex_color};")


