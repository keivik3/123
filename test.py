import unittest
from unittest import mock
from network import Network
from game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game(1)

    def test_initial_state(self):
        self.assertFalse(self.game.p1Went)
        self.assertFalse(self.game.p2Went)
        self.assertFalse(self.game.ready)
        self.assertEqual(self.game.id, 1)
        self.assertEqual(self.game.moves, [None, None])
        self.assertEqual(self.game.wins, [0, 0])
        self.assertEqual(self.game.ties, 0)

    def test_get_player_move(self):
        self.game.moves = ['R', 'P']
        self.assertEqual(self.game.get_player_move(0), 'R')
        self.assertEqual(self.game.get_player_move(1), 'P')

    def test_play(self):
        self.game.play(0, 'R')
        self.assertEqual(self.game.moves[0], 'R')
        self.assertTrue(self.game.p1Went)
        self.assertFalse(self.game.p2Went)

        self.game.play(1, 'P')
        self.assertEqual(self.game.moves[1], 'P')
        self.assertTrue(self.game.p2Went)

    def test_connected(self):
        self.assertFalse(self.game.connected())

        self.game.ready = True
        self.assertTrue(self.game.connected())

    def test_bothWent(self):
        self.assertFalse(self.game.bothWent())

        self.game.p1Went = True
        self.assertFalse(self.game.bothWent())

        self.game.p2Went = True
        self.assertTrue(self.game.bothWent())

    def test_winner(self):
        self.game.moves = ['R', 'S']
        self.assertEqual(self.game.winner(), 0)

        self.game.moves = ['S', 'R']
        self.assertEqual(self.game.winner(), 1)

        self.game.moves = ['P', 'R']
        self.assertEqual(self.game.winner(), 0)

        # Add more test cases for other combinations of moves

    def test_resetWent(self):
        self.game.p1Went = True
        self.game.p2Went = True

        self.game.resetWent()

        self.assertFalse(self.game.p1Went)
        self.assertFalse(self.game.p2Went)


class TestNetwork(unittest.TestCase):

    def test_getP(self):
        network = Network()
        network.p = "Connected"
        self.assertEqual(network.getP(), "Connected")

    def test_connect_failure(self):
        network = Network()
        with mock.patch('socket.socket') as mock_socket:
            mock_client = mock_socket.return_value
            mock_client.connect.side_effect = Exception("Connection failed")
            response = network.connect()
            self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
