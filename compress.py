




class Compress:
    

    def __init__(self):
        self.dictionary = {}
        self.num_list = []
        self.text_from_file = ""


    def compress(self, text):

        con = 1

        for elem in text.split(" "):

            if elem not in self.dictionary.keys(): #si la palabra no esta en el diccionario la agrego al diccionario
                self.dictionary[elem] = con
                con += 1
            
            self.num_list.append(self.dictionary[elem]) #agrega el valor de la palabra
        
        return self.num_list, self.dictionary # retorno la lista y el diccionario


    def uncompress(self, lista_num, diccio):

        for i in lista_num: 
            for key, value in diccio.items():

                if value == i: #si el valor de la palabra es igual al valor de la lista lo meto al texto
                    self.text_from_file += self.text_from_file.join([key + " "]) #agrego el espacio para que no quede pegado el texto
        
        self.text_from_file = self.text_from_file.rstrip() #quito los espacios al final
        
        return self.text_from_file


if __name__ == "__main__":
    pass
