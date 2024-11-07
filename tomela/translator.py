from transformers import MarianMTModel, MarianTokenizer

def translator(latin_text, hg_model='Helsinki-NLP/opus-mt-ROMANCE-en'):
    # Load the model and tokenizer for Latin to English translation
    tr_model_name = hg_model
    tr_tokenizer = MarianTokenizer.from_pretrained(tr_model_name)
    tr_model = MarianMTModel.from_pretrained(tr_model_name)


    # Prepare the text for translation
    batch = tr_tokenizer([latin_text], return_tensors="pt")

    # Perform translation
    translated = tr_model.generate(**batch)
    translation = tr_tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translation[0]