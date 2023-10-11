import galai as gal

def main():
    model = gal.load_model("huge")
    model.generate("The Transformer architecture [START_REF]")
    # The Transformer architecture [START_REF] Attention is All you Need, Vaswani[END_REF] has been widely used in natural language processing.
    #https://github.com/paperswithcode/galai/blob/3a724f562af1a0c8ff97a096c5fbebe579e2160f/notebooks/Introduction%20to%20Galactica%20Models.ipynb
    #

if __name__ == '__main__':
    main()