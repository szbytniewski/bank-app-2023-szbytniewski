import datetime
import unittest
from unittest.mock import MagicMock

from ..KontoFirmowe import KontoFirmowe
from ..KontoOsobiste import KontoOsobiste
from ..SMTPConnection import SMTPConnection


class TestHistory(unittest.TestCase):
    connection = SMTPConnection

    receiver_email = "example@gmail.com"
    today_date = datetime.date.today().strftime("%Y-%m-%d")


    mock_validate_nip_response = {
        'result': {
            'subject': {
                'nip': '8461627563',
            },
        }
    }

    def test_send_private_account_history_true(self):
        mock_send = MagicMock()
        mock_send.return_value = True

        account = KontoOsobiste("Adam", "Nowak", "01282874666")

        with MagicMock() as mock_smtp_connection:
            mock_smtp_connection.wyslij = mock_send
            result = account.wyslij_historie_na_maila(self.receiver_email, mock_smtp_connection)

        self.assertTrue(result)


        mock_send.assert_called_once_with(f"Wyciąg z dnia {self.today_date}", f"Twoja historia konta to: {account.history}", self.receiver_email)

    def test_send_private_account_history_false(self):
        mock_send = MagicMock()
        mock_send.return_value = False

        account = KontoOsobiste("Adam", "Nowak", "01282874666")

        with MagicMock() as mock_smtp_connection:
            mock_smtp_connection.wyslij = mock_send
            result = account.wyslij_historie_na_maila(self.receiver_email, mock_smtp_connection)

        self.assertFalse(result)


        mock_send.assert_called_once_with(f"Wyciąg z dnia {self.today_date}", f"Twoja historia konta to: {account.history}", self.receiver_email)

    def test_send_company_history_true(self):
        mock_send = MagicMock()
        mock_send.return_value = True

        mock_get = MagicMock()
        mock_get.json.return_value = self.mock_validate_nip_response

        account = KontoFirmowe("Dziam dziam", "8461627563")

        with MagicMock() as mock_smtp_connection, MagicMock() as mock_requests_get:
            mock_smtp_connection.wyslij = mock_send
            mock_requests_get.return_value = mock_get
            result = account.wyslij_historie_na_maila(self.receiver_email, mock_smtp_connection)

        self.assertTrue(result)

        mock_send.assert_called_once_with(f"Wyciąg z dnia {self.today_date}", f"Historia konta Twojej firmy to: {account.history}", self.receiver_email)

    def test_send_company_history_false(self):
        mock_send = MagicMock()
        mock_send.return_value = False

        mock_get = MagicMock()
        mock_get.json.return_value = self.mock_validate_nip_response

        account = KontoFirmowe("Dziam dziam", "8461627563")

        with MagicMock() as mock_smtp_connection, MagicMock() as mock_requests_get:
            mock_smtp_connection.wyslij = mock_send
            mock_requests_get.return_value = mock_get
            result = account.wyslij_historie_na_maila(self.receiver_email, mock_smtp_connection)

        self.assertFalse(result)

        mock_send.assert_called_once_with(f"Wyciąg z dnia {self.today_date}", f"Historia konta Twojej firmy to: {account.history}", self.receiver_email)
