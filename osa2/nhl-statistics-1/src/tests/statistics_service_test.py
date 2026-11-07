import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Semenko")
        self.assertIsNotNone(pelaaja)
        self.assertEqual(pelaaja.name, "Semenko")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.stats.search("jokuPelaaja")
        self.assertIsNone(pelaaja)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        edm_pelaajat = self.stats.team("EDM")
        self.assertEqual(len(edm_pelaajat), 3)
        self.assertEqual(edm_pelaajat[0].name, "Semenko")

    def test_top_palauttaa_eniten_pisteita_tehneet(self):
        parhaat = self.stats.top(2)
        self.assertEqual(len(parhaat), 3)
        self.assertEqual(parhaat[0].name, "Gretzky")
        self.assertEqual(parhaat[1].name, "Lemieux")
        self.assertEqual(parhaat[2].name, "Yzerman")
