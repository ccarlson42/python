from television import *


class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0, Muted = False'
        self.tv = Television()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"


    def test_power(self):
        self.tv.power()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = False"

    def test_mute(self):
        self.tv.power()  # Turn TV on first
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = False"
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = True"
        self.tv.power()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = True"
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"


    def test_channel_up(self):
        self.tv.channel_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0, Muted = False"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = False"




    def test_channel_down(self):
        self.tv.channel_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0, Muted = False"




    def test_volume_up(self):
        self.tv.volume_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1, Muted = False"
        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2, Muted = False"
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2, Muted = False"



    def test_volume_down(self):
        self.tv.volume_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0, Muted = False"
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1, Muted = False"
        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = False"
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0, Muted = False"









