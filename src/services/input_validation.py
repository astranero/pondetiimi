import re

class InputValidation:
    ''' Syötteiden validointi. '''

    @classmethod
    def isbn(cls, input_string):
        '''
        Tarkistetaan ISBN-syötteen oikellisuutta. ISBN syöte on 13 tai 10 merkkiä pitkä ja
        on oikeassa formaatissa.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        # tämä ei ole kaiken kattava ratkaisu, mutta toimii useimmissa tapauksissa
        # laatimisessa käytetty virallista ohjetta täällä:
        # https://www.isbn-international.org/sites/default/files/ISBN-k%C3%A4ytt%C3%B6opas%20%28Finnish%20translation%20of%20seventh%20edition%29_0.pdf

        # tarkista syotteen muoto, eli numeroiden määrä eri osissa
        regexp = "^(97(8|9)[- ]?)?\\d{1,5}[- ]?\\d{1,7}[- ]?\\d{1,6}[- ]?\\d$"
        if not re.match(regexp, input_string):
            return False

        pelkat_numerot = input_string.replace("-", "").replace(" ", "")
        return len(pelkat_numerot) in [10, 13]

    @classmethod
    def year(cls, input_string):
        '''
        Tarkistetaan Year-syötteen oikellisuutta. Syöte on muotoa 4 lukua.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^\\d{4}$", input_string) is not None

    @classmethod
    def name(cls, input_string):
        '''
        Tarkistetaan Author-syöte. Syöte on muotoa "Sukunimi, Etunimi; Sukunimi, Etunimi..."
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        # hyväksytään kaikki merkkijonot
        return re.match("^([A-ZÄÖ][a-zäö]+, [A-ZÄÖ][a-zäö]+;? ?)+$", input_string) is not None

    @classmethod
    def menu_command(cls, input_string):
        '''
        Tarkistetaan Menu-syöte. Syöte on luku 0 - 4.
        Args:
            input_string (String): annettu syöte
        Returns
            (Boolean): True, jos syöte täyttää vaatimuksen.
        '''
        return re.match("^(0|1|2|3|4)$", input_string) is not None

    @classmethod
    def not_empty(cls, input_string):
        return re.match(".+", input_string) is not None