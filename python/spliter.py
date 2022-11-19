def split(string):
    encoded = string.encode('utf-8')
    full_length = len(encoded)

    no_dot = string.split(".")

    sentences = []
    for item in no_dot:
        sentences.append(item + '.')

    return sentences

    ##if full_length <= 5000:
    #    return [string]
#
    #else:
    ## 5000 is the incriment, 0 is the start
    #    info = []
    #    for i in range(0, full_length, 5000):
    #        try:
    #           info.append(encoded[i:i+5000])
    #        except:
    #            info.append(encoded[i:])
    #            print("Done!")
    #    print(info)
    #    return info