import unittest
import Persona

class TestPersona(unittest.TestCase):

    def test_get_Information(self):
        persona1 = Persona.Persona("Hector Humberto", "Lara", "Salas")
        resultado = persona1.get_str_information()
        self.assertEqual(resultado,"Hector Humberto Lara Salas")

if __name__ == "__main__":
    unittest.main()