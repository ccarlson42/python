#This is the code for a tv remote.
class Television():
    # Class Variables

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        This function sets the variables of the remote at start.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__last_volume = self.__volume

    # Methods

    def power(self) -> None:
        """
        This function powers the TV on/off
        :return:
        The TV on/off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        This function mutes/unmutes the TV.
        :return:
        Muting or unmuting the TV.
        """
        if self.__status:
            if not self.__muted:
                self.__last_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            if self.__muted:
                self.__volume = self.__last_volume

        self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        This function goes up channels on the TV.
        :return:
        The channel up.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        This function goes down channels on the TV.
        :return:
        The channel down.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        This function turns up volume on the TV.
        :return:
        The volume up.
        """
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
                self.__volume = self.__last_volume

            if self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This function turns down volume on the TV.
        :return:
        The volume down.
        """
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
                self.__volume = self.__last_volume

            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This function details the status of the TV's power, channel, volume, and if it is muted or not.
        :return:
        Return the status of the TV's power, channel, volume, and if it is muted or not.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}, Muted = {self.__muted}'
