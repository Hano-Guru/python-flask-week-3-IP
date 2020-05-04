import unittest
from app.models import Pitches
from app import db

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch=Pitches(pitch="covid19",author="hano",title="corona",id=12)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitches))
    def test_init(self):
        self.assertEqual(self.new_pitch.pitch,"covid19")
        self.assertEqual(self.new_pitch.author,"hano")
        self.assertEqual(self.new_pitch.title,"corona")
        self.assertEqual(self.new_pitch.id,12)
