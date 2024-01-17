class PrintQueue:
    def __init__(self):
        self.queue = list()
        
    def add_job(self, job):
        self.queue.append(job)  # Adding a print job to the end of the queue
        print(f"Added '{job}' to the print queue.")

    def process_jobs(self):
        if self.queue:
            print(f"Printing: '{self.queue[0]}'")  # Printing the first job in the queue
            del self.queue[0]  # Removing the printed job from the queue
        else:
            print("No more print jobs in the queue.")

# Creating an instance of PrintQueue
printer = PrintQueue()

# Simulating print job requests
printer.add_job("Document1")
printer.add_job("Presentation")
printer.add_job("Report")

# Processing print jobs
printer.process_jobs() 
printer.process_jobs()  
printer.process_jobs() 
printer.process_jobs()
