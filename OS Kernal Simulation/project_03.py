from tkinter import *
import time
from threading import Semaphore
from collections import deque
import math
#from PIL import ImageTk,Image
root = Tk()
root.title("OS Kernal Simulation")
#root.configure(bg="#85C1E9")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to the screen size
root.geometry(f"{screen_width}x{screen_height}")
global pcbdata, widgets, keyss, fcfs_widgets, short_widgets, keyss_short, Main_memory, memory_dict,memory_list,pages,Process_keys
Main_memory = 1000
memory_dict = {}
pcbdata={'1':['ready','2','11','17','24','ALU'],
         '2':['ready','2','3','7','24','MDR']}
# pcbdata = {}
widgets = []
keyss = []
fcfs_widgets = []
keyss_short = []
short_widgets = []
memory_list = []
pages = []
Process_keys = []
#main menu class i.e. Process, Memory, I/O Management
class Main_Menu:
    def __init__(self, root):
        self.blank_label = Label(root, text='', height=2)
        self.blank_label.pack()

        self.label_title = Label(root, text="OS Kernal Simulation", font="Times 36 italic bold")
        self.label_title.pack()

        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()

        def process_manage():
            self.destroy_elements_main()
            p_m = ProcessManagement()

        self.btn_Process_m = Button(root, text="Process Management", command=process_manage, fg="White", bg="Red")
        self.btn_Process_m.configure(width=50, height=2)
        self.btn_Process_m.pack()

        def memory_manage():
            self.destroy_elements_main()
            mem_m = MemoryManagement()

        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()

        self.btn_memory_m = Button(root, text="Memory Management", command=memory_manage, fg="White", bg="Black")
        self.btn_memory_m.configure(width=50, height=2)
        self.btn_memory_m.pack()

        def io_manage():
            self.destroy_elements_main()
            io_m = IO_Management()

        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()

        self.btn_io_m = Button(root, text="I/O Management", command=io_manage, fg="White", bg="Blue")
        self.btn_io_m.configure(width=50, height=2)
        self.btn_io_m.pack()

        def synchronization_func():
            self.destroy_elements_main()
            sync = synchronization()

        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()

        self.btn_sync = Button(root, text="Synchronization", command=synchronization_func, fg="Black", bg="Green")
        self.btn_sync.configure(width=50, height=2)
        self.btn_sync.pack()

    def destroy_elements_main(self):
        self.label_title.destroy()
        self.blank_label.destroy()
        self.blank_label1.destroy()
        self.blank_label2.destroy()
        self.btn_Process_m.destroy()
        self.blank_label3.destroy()
        self.btn_memory_m.destroy()
        self.btn_io_m.destroy()
        self.btn_sync.destroy()
        self.blank_label4.destroy()

#Class of Process Management
class ProcessManagement:
    def __init__(self):
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()

        self.label_title = Label(root, text="Process Management log", font="Times 24 bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()

        def create_process():
            self.destroy_elements()
            cc = Create()
        self.create_process = Button(root, text="Create Process", command=create_process, fg="Black", bg="#E74C3C")
        self.create_process.configure(width=50, height=2)
        self.create_process.pack()
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()

        def destroy_process():
            self.destroy_elements()
            dp = destroyProcess()
        self.destroy_process = Button(root, text="Destroy Process", command=destroy_process, fg="Black", bg="#EB984E")
        self.destroy_process.configure(width=50, height=2)
        self.destroy_process.pack()
        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()

        def suspend_process():
            self.destroy_elements()
            sp = suspendprocess()

        self.suspend_process = Button(root, text="Suspend Process", command=suspend_process, fg="Black", bg="#EB984E")
        self.suspend_process.configure(width=50, height=2)
        self.suspend_process.pack()
        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()

        def resume_process():
            self.destroy_elements()
            rp = resume_process_block()

        self.resume_process = Button(root, text="Resume Process", command=resume_process, fg="Black", bg="#EB984E")
        self.resume_process.configure(width=50, height=2)
        self.resume_process.pack()
        self.blank_label5 = Label(root, text='', height=1)
        self.blank_label5.pack()

        def change_process_priority():
            self.destroy_elements()
            cpp = process_priority_change()

        self.process_priority = Button(root, text="Change Process Priority", command=change_process_priority, fg="Black", bg="#EB984E")
        self.process_priority.configure(width=50, height=2)
        self.process_priority.pack()
        self.blank_label7 = Label(root, text='', height=1)
        self.blank_label7.pack()

        def dispatch_process():
            self.destroy_elements()
            das = dispatch_and_scheduling()

        self.dispatchPro = Button(root, text="Dispatch Process", command=dispatch_process, fg="Black", bg="#EB984E")
        self.dispatchPro.configure(width=50, height=2)
        self.dispatchPro.pack()
        self.blank_label8 = Label(root, text='', height=1)
        self.blank_label8.pack()

        def show_process():
            self.destroy_elements()
            sp = Show_Processes()

        self.ShowPro = Button(root, text="Show Processes", command=show_process, fg="Black", bg="#EB984E")
        self.ShowPro.configure(width=50, height=2)
        self.ShowPro.pack()
#----------------------------------------------------------------------------------------------------------------------------------------------
        def back_main():
            self.destroy_elements()
            mm = Main_Menu(root)

        self.blank_label6 = Label(root, text='', height=2)
        self.blank_label6.pack()
        self.back_to_main = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=back_main)
        self.back_to_main.configure(bd=2)
        self.back_to_main.pack()

    def destroy_elements(self):
        self.label_title.destroy()
        self.blank_label1.destroy()
        self.blank_label.destroy()
        self.create_process.destroy()
        self.destroy_process.destroy()
        self.suspend_process.destroy()
        self.resume_process.destroy()
        self.process_priority.destroy()
        self.blank_label2.destroy()
        self.blank_label3.destroy()
        self.blank_label4.destroy()
        self.blank_label5.destroy()
        self.blank_label7.destroy()
        self.dispatchPro.destroy()
        self.ShowPro.destroy()
        self.blank_label8.destroy()
        self.back_to_main.destroy()
        self.blank_label6.destroy()

#Class of Memory Management
class MemoryManagement:
    def __init__(self):
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()
        self.label_title = Label(root, text="Memory Management Block", font="Times 24 bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()
        self.pagesize_l = Label(root, text='Enter Page Size: ')
        self.pagesize_l.pack()
        self.page_s_in = Entry(root, width=20)
        self.page_s_in.pack()
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
        self.submit = Button(root, text="Submit", command=self.paging)
        self.submit.configure(width=50, height=2)
        self.submit.pack()
        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()
        self.lruimpl = Button(root, text="Implement LRU", command=self.LRU)
        self.lruimpl.configure(width=50, height=2)
        self.lruimpl.pack()

    def destroy_elements_for_paging(self):
        self.blank_label2.destroy()
        self.blank_label1.destroy()
        self.blank_label.destroy()
        self.pagesize_l.destroy()
        #self.label_title.destroy()
        self.page_s_in.destroy()
        self.blank_label3.destroy()
        self.lruimpl.destroy()
        self.submit.destroy()
    def paging(self):

        self.page_size = int(self.page_s_in.get())
        for key in pcbdata.keys():
            Process_keys.append(key)
        for key, value in pcbdata.items():
            memory_dict[key] = value[4]
        for value in memory_dict.values():
            memory_list.append(value)
        self.process_size = list(map(int, memory_list))
        for i in self.process_size:
            self.no_of_pages = i // self.page_size
            if i % self.page_size != 0:
                self.no_of_pages += 1
            pages.append(self.no_of_pages)
        #     print(no_of_pages)
        # print(pages)
        for keys, i in zip(memory_dict.keys(), pages):
            for j in range(i):
                self.show_pages = Label(root, text='Process '+ keys+' :'+' Page: '+ str(j))
                self.show_pages.pack()
        self.destroy_elements_for_paging()
    def LRU(self):
        self.framel = Label(root, text='Enter Frame Number: ')
        self.framel.pack()
        self.framesize = Entry(root, width=20)
        self.process_string = [1, 2, 1, 3, 4, 2, 4, 3, 1, 2]
        q = deque()
        for i in range(len(self.process_string)):
            if len(q) == 4:
                q.popleft()
            q.append(self.process_string[i])
            self.listofq = str(list(q))
            self.lruprint = Label(root, text=self.listofq)
            self.lruprint.pack()
            #print(list(q))
class IO_Management:
    def __init__(self):
        self.manage_label = Label(root, text="memory Management Block")
        self.manage_label.pack()
class Create:
    def __init__(self):
        self.registers = ['ACC', 'MDR', 'MAR', 'CIR']
        self.selected_register = StringVar()
        self.selected_register.set('ACC')
        self.selected_value = StringVar()
        self.options = ['Ready']
        self.selected_value.set('Ready')
        self.blank_label5 = Label(root, text='', height=3)
        self.blank_label5.pack()
        self.idl = Label(root, text='Enter ID:')
        self.idl.pack()
        self.id = Entry(root, width=20)
        self.id.pack()
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
        self.statel = Label(root, text='Enter Current State:')
        self.statel.pack()
        self.state = OptionMenu(root, self.selected_value, *self.options)
        self.state.pack()
        self.blank_label1 = Label(root, text='', height=1)
        self.blank_label1.pack()
        self.priorityl = Label(root, text='Enter Current Priority: (1-10)')
        self.priorityl.pack()
        self.priority = Entry(root, width=40)
        self.priority.pack()
        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()
        self.arrivaltl = Label(root, text='Enter Arrival Time: ')
        self.arrivaltl.pack()
        self.arrivalt = Entry(root, width=40)
        self.arrivalt.pack()
        self.blank_label7 = Label(root, text='', height=1)
        self.blank_label7.pack()
        self.burstl = Label(root, text='Enter Process Burst Time:')
        self.burstl.pack()
        self.burstin = Entry(root, width=40)
        self.burstin.pack()
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()
        self.memory_reql = Label(root, text='Enter Memory Space Required:')
        self.memory_reql.pack()
        self.memory_req = Entry(root, width=40)
        self.memory_req.pack()
        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()
        self.register = OptionMenu(root, self.selected_register, *self.registers)
        self.register.pack()
        self.createbtn = Button(root, text='CREATE PROCESS', padx=50, command=self.validation, fg="White", bg='Dark Green', font='Times 20 bold')
        self.createbtn.pack()
        self.blank_label6 = Label(root, text='', height=1)
        self.blank_label6.pack()
        self.back_to_process = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=self.back_to_process_log)
        self.back_to_process.configure(bd=2)
        self.back_to_process.pack()

    def validation(self):
        self.aa = int(self.priority.get())
        if self.id.get() in pcbdata.keys():
            self.id.delete(0, 'end')
        elif self.aa not in range(1,11):
            self.priority.delete(0, 'end')
        elif self.arrivalt.get() > self.burstin.get():
            self.arrivalt.delete(0, 'end')
            self.burstin.delete(0, 'end')
        else:
            self.createfunc()
    def createfunc(self):

        valueslist = []
        valueslist.append(self.selected_value.get())
        valueslist.append(self.priority.get())
        valueslist.append(self.arrivalt.get())
        valueslist.append(self.burstin.get())
        valueslist.append(self.memory_req.get())
        valueslist.append(self.selected_register.get())
        key = self.id.get()
        pcbdata[key] = valueslist
        #display = Label(root, text=pcbdata).pack()
        #back to processmanagement block
        self.destroy_create_elements()
        pm = ProcessManagement()
        return pcbdata
    def back_to_process_log(self):
        self.destroy_create_elements()
        pm1 = ProcessManagement()

    def destroy_create_elements(self):
        self.blank_label.destroy()
        self.blank_label7.destroy()
        self.createbtn.destroy()
        self.blank_label2.destroy()
        self.blank_label3.destroy()
        self.blank_label4.destroy()
        self.blank_label5.destroy()
        self.blank_label1.destroy()
        self.blank_label6.destroy()
        self.state.destroy()
        self.statel.destroy()
        self.priority.destroy()
        self.priorityl.destroy()
        self.id.destroy()
        self.idl.destroy()
        self.burstl.destroy()
        self.burstin.destroy()
        self.arrivaltl.destroy()
        self.arrivalt.destroy()
        self.memory_reql.destroy()
        self.memory_req.destroy()
        self.back_to_process.destroy()
        self.register.destroy()
class destroyProcess:
    def __init__(self):
        self.blank_label = Label(root, text='', height=3)
        self.blank_label.pack()
        self.didl = Label(root, text='Enter Process ID to Delete:')
        self.didl.pack()
        self.did = Entry(root, width=10)
        self.did.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()
        self.destroybtn = Button(root, text='Destroy Process', command=self.destroypf, padx=40, fg="White", bg='Dark Green', font='Times 20 bold')
        self.destroybtn.pack()
        self.blank_label2 = Label(root, text='', height=2)
        self.blank_label2.pack()
        self.back_to_process = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=self.back_to_pr_log)
        self.back_to_process.configure(bd=2)
        self.back_to_process.pack()

    def destroypf(self):
        if self.did.get() in pcbdata.keys():
            del pcbdata[self.did.get()]
            #processfound = Label(root, text='Process Deleted').pack()
            #ppupdate = Label(root, text=pcbdata).pack()
            self.destroy_destroy_elements()
            ppm = ProcessManagement()
        else:
            self.noprocess = Label(root, text='There is no such Process')
            self.noprocess.pack()
        return pcbdata
    def back_to_pr_log(self):
        self.destroy_destroy_elements()
        pm1 = ProcessManagement()
    def destroy_destroy_elements(self):
        self.blank_label.destroy()
        self.didl.destroy()
        self.did.destroy()
        self.blank_label1.destroy()
        self.destroybtn.destroy()
        self.back_to_process.destroy()
        self.blank_label2.destroy()
class suspendprocess:
    def __init__(self):
        self.blank_label = Label(root, text='', height=3)
        self.blank_label.pack()
        self.susppl = Label(root, text='Enter Process ID to Suspend:')
        self.susppl.pack()
        self.suspp = Entry(root, width=20)
        # self.did.grid(row=5, column=5)
        self.suspp.pack()
        self.blank_label1 = Label(root, text='', height=3)
        self.blank_label1.pack()
        self.suspendbtn = Button(root, text='Suspend Process', command=self.suspendpro, padx=40, fg="White", bg='Dark Green', font='Times 20 bold')
        self.suspendbtn.pack()
        self.blank_label2 = Label(root, text='', height=2)
        self.blank_label2.pack()
        self.back_to_process = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=self.back_to_pr_log)
        self.back_to_process.configure(bd=2)
        self.back_to_process.pack()
    def suspendpro(self):
        if self.suspp.get() in pcbdata.keys():
            state = pcbdata[self.suspp.get()]
            state[0] = 'Blocked'
            pcbdata[self.suspp.get()] = state
            self.destroy_suspend_elements()
            pmm = ProcessManagement()
            #process suspend---back option

        else:
            self.noprocess = Label(root, text='No such Process')
            self.noprocess.pack()
        return pcbdata
    def back_to_pr_log(self):
        self.destroy_suspend_elements()
        pm1 = ProcessManagement()
    def destroy_suspend_elements(self):
        self.blank_label.destroy()
        self.susppl.destroy()
        self.suspp.destroy()
        self.blank_label1.destroy()
        self.suspendbtn.destroy()
        self.back_to_process.destroy()
        self.blank_label2.destroy()
class process_priority_change:
    def __init__(self):
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
        self.ppchangel = Label(root, text='Enter Process ID to Change Priority:')
        self.ppchangel.pack()
        self.ppchange = Entry(root, width=20)
        self.ppchange.pack()
        self.blank_label1 = Label(root, text='', height=1)
        self.blank_label1.pack()
        self.ppchnagebtn = Button(root, text='Change Process Priority', command=self.propri, padx=40, fg="White", bg='Dark Green', font='Times 20 bold')
        self.ppchnagebtn.pack()
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()

        self.back_to_process1 = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_to_pro_log)
        self.back_to_process1.configure(bd=2)
        self.back_to_process1.pack()
    def propri(self):
        if self.ppchange.get() in pcbdata.keys():
            prepriority = pcbdata[self.ppchange.get()]
            self.previouspriority = Label(root, text='Previous Priority: '+prepriority[1])
            self.previouspriority.pack()
            self.blank_label3 = Label(root, text='', height=1)
            self.blank_label3.pack()
            self.newpriority = Label(root, text='Enter New Priority: ')
            self.newpriority.pack()
            self.newpriorityin = Entry(root, width=20)
            self.newpriorityin.pack()
            self.blank_label5 = Label(root, text='', height=1)
            self.blank_label5.pack()
            self.updatebtn = Button(root, text='Update Priority', command=self.processpchange)
            self.updatebtn.pack()
            self.blank_label4 = Label(root, text='', height=1)
            self.blank_label4.pack()
            self.cancelchange = Button(root, text='Cancel', command=self.cancelchng, font='Times 16 bold', fg='Black', bg='Yellow')
            self.cancelchange.pack()
            self.destroy_priority_elements()
        else:
            self.noprocess = Label(root, text='No such Process')
            self.noprocess.pack()
            self.destroy_priority_elements()

    def cancelchng(self):
        self.previouspriority.destroy()
        self.blank_label3.destroy()
        self.newpriority.destroy()
        self.newpriorityin.destroy()
        self.updatebtn.destroy()
        self.blank_label4.destroy()
        self.cancelchange.destroy()
        self.blank_label5.destroy()
        self.ppchange.destroy()
        self.ppchangel.destroy()
        #self.noprocess.destroy()
        pm2 = ProcessManagement()
    def pp_updated(self):
        data_list = pcbdata[self.ppchange.get()]
        data_list[1] = self.newpriorityin.get()
        pcbdata[self.ppchange.get()] = data_list
        #return pcbdata
    def processpchange(self):
        self.pp_updated()
        self.cancelchng()
    def back_to_pro_log(self):
        self.destroy_priority_elements()
        pm2 = ProcessManagement()
    def destroy_priority_elements(self):
        self.blank_label.destroy()
        self.blank_label1.destroy()
        #self.ppchangel.destroy()
        #self.ppchange.destroy()
        self.ppchnagebtn.destroy()
        self.blank_label2.destroy()
        self.back_to_process1.destroy()
class Show_Processes:

    def __init__(self):
        self.black_label = Label(root, text='', height=2)
        self.black_label.pack()
        self.show_by_id = Button(root, text='Show Process By ID', command=self.show_by_id_func, padx=40, fg='Black', bg='Pink')
        self.show_by_id.pack()
        self.black_label1 = Label(root, text='', height=2)
        self.black_label1.pack()
        self.show_all = Button(root, text='Show All Process', command=self.show_all_process, padx=45, fg='Black', bg='Pink')
        self.show_all.pack()
        self.black_label2 = Label(root, text='', height=2)
        self.black_label2.pack()
        self.back_to_process1 = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=self.back_to_pro_log)
        self.back_to_process1.configure(bd=2)
        self.back_to_process1.pack()
    def back_to_pro_log(self):
        self.black_label.destroy()
        self.black_label1.destroy()
        self.black_label2.destroy()
        self.show_by_id.destroy()
        self.show_all.destroy()
        self.back_to_process1.destroy()
        pm = ProcessManagement()
    def back_in_show_id(self):
        self.enteridl.destroy()
        self.enterid.destroy()
        self.show_id_pro.destroy()
        self.black_label3.destroy()
        self.black_label4.destroy()
        self.back_to_process3.destroy()
        self.state.destroy()
        self.priority.destroy()
        self.arrival_time.destroy()
        self.burst_time.destroy()
        self.memory_space.destroy()
        self.registers_l.destroy()
        pm = ProcessManagement()
    def back_in_show_id_1(self):
        self.enteridl.destroy()
        self.enterid.destroy()
        self.show_id_pro.destroy()
        self.black_label3.destroy()
        self.black_label4.destroy()
        self.back_to_process3.destroy()
        pm = ProcessManagement()
    def show_by_id_func(self):
        self.black_label.destroy()
        self.black_label1.destroy()
        self.black_label2.destroy()
        self.show_by_id.destroy()
        self.show_all.destroy()
        self.back_to_process1.destroy()
        self.enteridl = Label(root, text='Enter ID: ')
        self.enteridl.pack()
        self.enterid = Entry(root, width=20)
        self.enterid.pack()
        self.black_label3 = Label(root, text='', height=2)
        self.black_label3.pack()
        self.show_id_pro = Button(root, text='Show Data', command=self.id_search)
        self.show_id_pro.pack()
        self.black_label4 = Label(root, text='', height=2)
        self.black_label4.pack()
        self.back_to_process3 = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=self.back_in_show_id_1)
        self.back_to_process3.configure(bd=2)
        self.back_to_process3.pack()
    def id_search(self):
        if self.enterid.get() in pcbdata.keys():
            list_of_data = pcbdata[self.enterid.get()]
            self.state = Label(root, text='State: '+list_of_data[0])
            self.state.pack()
            self.priority = Label(root, text='Priority: '+list_of_data[1])
            self.priority.pack()
            self.arrival_time = Label(root, text='Arrival Time: '+list_of_data[2])
            self.arrival_time.pack()
            self.burst_time = Label(root, text='Burst Time: ' + list_of_data[3])
            self.burst_time.pack()
            self.memory_space = Label(root, text='Memory Space: '+list_of_data[4])
            self.memory_space.pack()
            self.registers_l = Label(root, text='Register: ' + list_of_data[5])
            self.registers_l.pack()
        else:
            self.noprocess = Label(root, text='No such Process')
            self.noprocess.pack()

    # __________________________________________
    def back_in_p_l(self):
        for items in widgets:
            items.destroy()
        self.back_to_process2.destroy()
        #self.noprocesssl.destroy()

        pml = ProcessManagement()

    def show_all_process(self):
        self.black_label.destroy()
        self.black_label1.destroy()
        self.black_label2.destroy()
        self.show_by_id.destroy()
        self.show_all.destroy()
        self.back_to_process1.destroy()
        for key, value in pcbdata.items():
            self.linelabel = Label(root, text='--------------------------')
            self.linelabel.pack()
            self.key = Label(root, text='ID: '+key)
            self.key.pack()
            list_of_data_id = pcbdata[key]
            self.statesl = Label(root, text='State: ' + list_of_data_id[0])
            self.statesl.pack()
            self.prioritysl = Label(root, text='Priority: ' + list_of_data_id[1])
            self.prioritysl.pack()
            self.arrival_timesl = Label(root, text='Arrival Time Time: ' + list_of_data_id[2])
            self.arrival_timesl.pack()
            self.burst_timesl = Label(root, text='Burst Time: ' + list_of_data_id[3])
            self.burst_timesl.pack()
            self.memory_spacesl = Label(root, text='Memory Space: ' + list_of_data_id[4])
            self.memory_spacesl.pack()
            self.registersl = Label(root, text='Register: ' + list_of_data_id[5])
            self.registersl.pack()
            widgets.append(self.linelabel)
            widgets.append(self.key)
            widgets.append(self.statesl)
            widgets.append(self.prioritysl)
            widgets.append(self.arrival_timesl)
            widgets.append(self.burst_timesl)
            widgets.append(self.memory_spacesl)
            widgets.append(self.registersl)
        # else:
        #     self.noprocesssl = Label(root, text='No Process is Created')
        #     self.noprocesssl.pack()
        self.back_to_process2 = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_in_p_l)
        self.back_to_process2.configure(bd=2)
        self.back_to_process2.pack()
#__________________________________________________________________
class resume_process_block:
    def __init__(self):
        self.blank_label = Label(root, text='', height=3)
        self.blank_label.pack()
        self.resupl = Label(root, text='Enter Process ID to Resume:')
        self.resupl.pack()
        self.resup = Entry(root, width=20)
        self.resup.pack()
        self.blank_label1 = Label(root, text='', height=3)
        self.blank_label1.pack()
        self.resumebtn = Button(root, text='Resume Process', command=self.resumepro, padx=40, fg="White",bg='Dark Green', font='Times 20 bold')
        self.resumebtn.pack()
        self.blank_label2 = Label(root, text='', height=2)
        self.blank_label2.pack()
        self.back_to_process = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_to_pr_log)
        self.back_to_process.configure(bd=2)
        self.back_to_process.pack()

    def back_to_pr_log(self):
        self.destroy_resume_elements()
        pm1 = ProcessManagement()

    def destroy_resume_elements(self):
        self.blank_label.destroy()
        self.resup.destroy()
        self.resupl.destroy()
        self.blank_label1.destroy()
        self.resumebtn.destroy()
        self.back_to_process.destroy()
        self.blank_label2.destroy()
    def resumepro(self):
        if self.resup.get() in pcbdata.keys():
            state = pcbdata[self.resup.get()]
            if state[0] == 'Blocked':
                state[0] = 'ready'
                pcbdata[self.resup.get()] = state
                pmm1 = ProcessManagement()
            else:
                self.noblocked = Label(root, text='No Process in Blocked State')
                self.noblocked.pack()
        else:
            self.noprocess = Label(root, text='No such Process')
            self.noprocess.pack()
        return pcbdata
#-------------------------------------------------------------------------
class dispatch_and_scheduling:
    def __init__(self):
        self.blank_label = Label(root, text='', height=2)
        self.blank_label.pack()
        self.fcfs = Button(root, text='FCFS', command=self.fcfs_func, padx=40, fg='White', bg='Black', height=2, font='Times 18 bold')
        self.fcfs.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()
        self.shortest_job = Button(root, text='SJS', command=self.shortest_job_func, padx=50, fg='White', bg='Black', height=2, font='Times 18 bold')
        self.shortest_job.pack()
        self.blank_label2 = Label(root, text='', height=2)
        self.blank_label2.pack()
        self.back_to_pro = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.backk)
        self.back_to_pro.configure(bd=2)
        self.back_to_pro.pack()
    def backk(self):
        self.blank_label.destroy()
        self.blank_label2.destroy()
        self.blank_label1.destroy()
        self.fcfs.destroy()
        self.shortest_job.destroy()
        self.back_to_pro.destroy()
        ppp = ProcessManagement()
    def back_btn(self):
        self.destroy_fcfs_shortest_buttons()
        pro = ProcessManagement()
    def fcfs_func(self):
        self.destroy_fcfs_shortest_buttons()
        self.arrival_data = []
        self.burst_data = []
        for value in pcbdata.values():
            self.arrival = value[2]
            self.arrival_data.append(self.arrival)
        for value in pcbdata.values():
            self.burst = value[3]
            self.burst_data.append(self.burst)
        self.arrival_time = list(map(int, self.arrival_data))
        self.burst_time = list(map(int, self.burst_data))
        for i in range(len(self.arrival_time)):
            self.minimum_value = min(self.arrival_time)
            self.first_process_index = self.arrival_time.index(self.minimum_value)
            self.burst_time_index = self.first_process_index
            self.arrival_value = self.arrival_time[self.first_process_index]
            self.burst_value = self.burst_time[self.burst_time_index]
            for i in range(self.arrival_value, self.burst_value):
                for key, value in pcbdata.items():
                    if str(self.arrival_value) in value:
                        # self.process_going = Label(root, text='Process in Progress: ' +key)
                        # self.process_going.pack()
                        time.sleep(2)
                        self.process_completed = Label(root, text='Process '+key+' done')
                        self.process_completed.pack()
                        keyss.append(key)
                        #fcfs_widgets.append(self.process_going)
                        fcfs_widgets.append(self.process_completed)
                break
            self.arrival_time.remove(self.arrival_value)
            self.burst_time.remove(self.burst_value)
        for i in keyss:
            del pcbdata[i]
        self.back_to_pm = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.destroy_fcfs_progress)
        self.back_to_pm.configure(bd=2)
        self.back_to_pm.pack()


    def destroy_fcfs_progress(self):
        for items in fcfs_widgets:
            items.destroy()
        self.back_to_pm.destroy()
        pmmm = ProcessManagement()
    def shortest_job_func(self):
        self.destroy_fcfs_shortest_buttons()
        self.arrival_data_s = []
        self.burst_data_s = []
        self.shortest_time = []
        for value in pcbdata.values():
            arrival = value[2]
            self.arrival_data_s.append(arrival)
        for value in pcbdata.values():
            burst = value[3]
            self.burst_data_s.append(burst)
        self.arrival_time_s = list(map(int, self.arrival_data_s))
        self.burst_time_s = list(map(int, self.burst_data_s))
        for i, j in zip(self.arrival_time_s, self.burst_time_s):
            shortest = j - i
            self.shortest_time.append(shortest)
        for i in range(len(self.shortest_time)):
            self.minimum_value_s = min(self.shortest_time)
            self.first_process_index_s = self.shortest_time.index(self.minimum_value_s)
            self.arrival_value_s = self.arrival_time_s[self.first_process_index_s]
            self.shortest_value = self.shortest_time[self.first_process_index_s]
            for i in range(self.shortest_value):
                self.sleep_value = 2
                for key, value in pcbdata.items():
                    if str(self.arrival_value_s) in value:
                        # self.process_going = Label(root, text='Process in Progress: ' + key)
                        # self.process_going.pack()
                        time.sleep(self.sleep_value)
                        self.process_completed = Label(root, text='Process ' + key + ' done')
                        self.process_completed.pack()
                        keyss_short.append(key)
                        #short_widgets.append(self.process_going)
                        short_widgets.append(self.process_completed)
                break
            self.shortest_time.remove(self.shortest_value)
        for i in keyss_short:
            del pcbdata[i]
        self.back_to_pm = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.destroy_shortest_job)
        self.back_to_pm.configure(bd=2)
        self.back_to_pm.pack()
    def destroy_shortest_job(self):
        for items in short_widgets:
            items.destroy()
        self.back_to_pm.destroy()
        pmmm = ProcessManagement()
    def destroy_fcfs_shortest_buttons(self):
        self.fcfs.destroy()
        self.shortest_job.destroy()
        self.blank_label.destroy()
        self.blank_label1.destroy()
        self.blank_label2.destroy()
        self.back_to_pro.destroy()


class synchronization:
    def __init__(self):
        key_resource = {}
        sync = {}
        # extract keys and resource names from pcbdata
        for key in pcbdata.keys():
            resource = pcbdata[key][5]
            key_resource.setdefault(resource, []).append(key)
        # create a dictionary with keys as resource names and values as lists of keys
        for resource, keys in key_resource.items():
            sync[resource] = keys
        resources = {'ALU': ['Resource1', 'Resource2', 'Resource3'], 'MDR': ['Resource4', 'Resource5'],
                     'MAR': ['Resource6']}
        Resource1_sem = Semaphore(1)
        Resource2_sem = Semaphore(1)
        Resource3_sem = Semaphore(1)
        Resource4_sem = Semaphore(1)
        Resource5_sem = Semaphore(1)
        Resource6_sem = Semaphore(1)

        output_label = Label(root, text="", font=("Arial", 12))
        output_label.pack()
        message = ""
        for resource, keys in sync.items():
            message += f"Processes {keys} are sharing the following resources: {resources[resource]}\n"
            for res in resources[resource]:
                eval(res + "_sem").acquire()
                message += res + " acquired\n"
                output_label.configure(text=message)
                root.update()
            for res in resources[resource]:
                eval(res + "_sem").release()
                message += res + " released\n"
                output_label.configure(text=message)
                root.update()


m_m = Main_Menu(root)
root.mainloop()