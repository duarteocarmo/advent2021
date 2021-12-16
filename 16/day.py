def to_binary(hex_string):
    end_length = len(hex_string) * 4
    hex_as_int = int(hex_string, 16)
    hex_as_binary = bin(hex_as_int)
    padded_binary = hex_as_binary[2:].zfill(end_length)

    return padded_binary


class Packet:
    def __init__(self, binary_content):
        self.bin = binary_content
        self.version = int(binary_content[0:3], 2)
        self.type_id = int(binary_content[3:6], 2)
        if self.type_id == 4:
            self.content = self.decode_literal()
        else:
            self.content = self.decode_operator()

    def decode_literal(self):
        lit_value = ""

        tracker = 6
        while True:
            start_bit = self.bin[tracker]
            values = self.bin[tracker + 1 : tracker + 5]
            lit_value += values

            if start_bit == "0":
                self.size = tracker + 5
                break

            tracker += 5

        return int(lit_value, 2)

    def decode_operator(self):
        length_type_id = self.bin[6]
        content = []

        if length_type_id == "0":
            self.size = 22 + int(self.bin[7:22], 2)
            to_read = self.bin[22 : self.size]
            while to_read:
                content.append(Packet(to_read))
                to_read = to_read[content[-1].size :]
        else:
            sub_count = int(self.bin[7:18], 2)
            to_read = self.bin[18:]
            for _ in range(sub_count):
                content.append(Packet(to_read))
                to_read = to_read[content[-1].size :]
            self.size = 18 + sum(packet.size for packet in content)
        return content

    @property
    def versions_sum(self):
        if self.type_id == 4:
            return self.version
        else:
            return self.version + sum(p.versions_sum for p in self.content)


puzzle = "820D4100A1000085C6E8331F8401D8E106E1680021708630C50200A3BC01495B99CF6852726A88014DC9DBB30798409BBDF5A4D97F5326F050C02F9D2A971D9B539E0C93323004B4012960E9A5B98600005DA7F11AFBB55D96AFFBE1E20041A64A24D80C01E9D298AF0E22A98027800BD4EE3782C91399FA92901936E0060016B82007B0143C2005280146005300F7840385380146006900A72802469007B0001961801E60053002B2400564FFCE25FEFE40266CA79128037500042626C578CE00085C718BD1F08023396BA46001BF3C870C58039587F3DE52929DFD9F07C9731CC601D803779CCC882767E668DB255D154F553C804A0A00DD40010B87D0D6378002191BE11C6A914F1007C8010F8B1122239803B04A0946630062234308D44016CCEEA449600AC9844A733D3C700627EA391EE76F9B4B5DA649480357D005E622493112292D6F1DF60665EDADD212CF8E1003C29193E4E21C9CF507B910991E5A171D50092621B279D96F572A94911C1D200FA68024596EFA517696EFA51729C9FB6C64019250034F3F69DD165A8E33F7F919802FE009880331F215C4A1007A20C668712B685900804ABC00D50401C89715A3B00021516E164409CE39380272B0E14CB1D9004632E75C00834DB64DB4980292D3918D0034F3D90C958EECD8400414A11900403307534B524093EBCA00BCCD1B26AA52000FB4B6C62771CDF668E200CC20949D8AE2790051133B2ED005E2CC953FE1C3004EC0139ED46DBB9AC9C2655038C01399D59A3801F79EADAD878969D8318008491375003A324C5A59C7D68402E9B65994391A6BCC73A5F2FEABD8804322D90B25F3F4088F33E96D74C0139CF6006C0159BEF8EA6FBE3A9CEC337B859802B2AC9A0084C9DCC9ECD67DD793004E669FA2DE006EC00085C558C5134001088E308A20"
binary = to_binary(puzzle)
thas = Packet(binary_content=binary)
print(thas.versions_sum)
