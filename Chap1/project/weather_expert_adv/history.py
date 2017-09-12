
class History(object):
    id = 1
    records={}

    def add_records(self,records):
        print('History 初始化后，添加记录前，History.records:', History.records)
        print('History 初始化后，添加记录前，self.records:', self.records)
        self.records[self.id] = records
        self.id += 1
        print('History 添加记录后，History.records:', History.records)
        print('History 添加记录后，self.records:', self.records)


    def show_records(self):
        if (len(self.records) == 0):
            print ("Not history records are found, please do some search and retry")
        else:
            for k,v in self.records.items():
                print(f"{k} {v}")

    @classmethod
    def show_records_cls(cls):
        if (len(cls.records) == 0):
            print ("Not history records are found, please do some search and retry")
        else:
            for k,v in cls.records.items():
                print(f"{k} {v}")
