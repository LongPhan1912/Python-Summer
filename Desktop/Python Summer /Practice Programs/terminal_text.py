## Create a Python project that will help to print
## colored text, bold, italic, faint, blink (slow/fast), on terminal window.
def custom_text(n,s):
	ansi_color={"bold":1,"faint":2,"italic":3,"underline":4,"blink_slow":5,"blink_fast":6,"negative":7,"conceal":8,"strike_th":9,
	"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,"cyan":36,"white":37,
	"b_black":40,"b_red":41,"b_green":42,"b_yellow":43,"b_blue":44,"b_magenda":45,"b_cyan":46,"b_white":47,}
	try:
		num=str(ansi_color[n])
		value="\033["+num+"m"+s+"\033[0m"
        # without the "\033[0m", the terminal will change according to the most recent call of the function
		return value
	except:
		pass

print (custom_text('bold',"Python Project"))
print (custom_text('italic',"Python Project"))
print (custom_text('blink_fast',"Python Project"))
print (custom_text('green',"Python Project"))
