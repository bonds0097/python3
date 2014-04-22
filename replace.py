string = 'fvoxoxfvwdepagxmwxfpukleofxhwevefuygzepfvexwfvufgeyfryedojhwffoyhxcwgmlxeylawfxfurwfvoxecfezfvwbecpfpeejuygoyfefvwxfpwwfxojumwuxfuffvwawuxflecaazubwjwoyfvwyepfvwuxfhwfjlopwckaohvfjlzopwoaahevupgwpfvuywjoywjdwyfufjupouvbuaajwuaoupkecygjwoyfvwuxxdofvyeacmwbvuzoyhlecpwzcbroyhdofvfvwgcgwdveheffvwrwlxfelecpxuzwuygfvexwfvufbuyfgempoyhxcofxbplfelecpcybawxujfexwffawgoxkcfwxfvechvflecgfubrawfvoxdofvuaoffawjepwfubfmcffvwyuhuoyzcghwkubrwpxogeyfryediubroxvwgufwupwswplfojwofvoyrezaorxuyhmcfxvofjuyfvwlpwubepkepufoeyuygojukwpxeyozobufoeyezzpwwgejzepuaaleczoaagebrwfxaorwfvufxubeybwkfzepwohyfeluaadvoawaudlwpxjcggldufwpuygfpexxfuaaecfezmcxoywxxoxiuoazepjwuyglecpwxcoyhjwbosoaalwnvomoffvoxoyfvwbecpfpeejheeygeofogupwlecbeyhpufcaufoeyxfvwzauhoxxoybwywdbplkfejohvfvuswyxumubrgeepxocxweagbplkfe'

replace = {'a':'d', 'b':'u', 'c':'c', 'd':'y', 'e':'A', 'f':'T', 'g':'l', 'h':'g',
    'i':'j', 'j':'w', 'k':'b', 'l':'m', 'm':'v', 'n':'x', 'o':'u', 'p':'n', 'q':'q',
    'r':'p', 's':'k', 't':'z', 'u':'o', 'v':'H', 'w':'E', 'x':'s', 'y':'r', 'z':'f'}

output = []

for char in string:
    output.append(replace[char])

output_string = "".join(output)
print(output_string)
