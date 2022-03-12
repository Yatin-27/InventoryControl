# -*- coding: utf-8 -*-
from os import path
import os.path
from tkinter import *
import csv
import random
import datetime
import os
from tkinter import messagebox
from matplotlib import pyplot as plt

from database import StockEntity

root = Tk()
root.title("Inventory Control")
root.iconbitmap("Logo.ico")
root.geometry("600x400")

# object for databse reads/writes
stockObj = StockEntity()


def createitem():
    # UI functionality for create item feature

    for widget in framei1_entry1.winfo_children():
        widget.destroy()

    # global name_entry,minQty_entry

    Label(framei1_entry1, text="Enter the name of item : ").grid(row=0, column=0)
    name_entry = Entry(framei1_entry1, width=50)
    name_entry.grid(row=0, column=1)

    Label(framei1_entry1, text="Enter the min qty of item needed: ").grid(
        row=1, column=0)
    minQty_entry = Entry(framei1_entry1, width=50)
    minQty_entry.grid(row=1, column=1)

    # global r
    r = IntVar()
    r.set("1")
    Radiobutton(framei1_entry1, text="Single multiplier",
                variable=r, value=1).grid(row=2, column=0, columnspan=2)
    Radiobutton(framei1_entry1, text="Dozen multiplier", variable=r,
                value=12).grid(row=3, column=0, columnspan=2)
    Radiobutton(framei1_entry1, text="Goods multiplier", variable=r,
                value=144).grid(row=4, column=0, columnspan=2)

    def onsubmit():
        # when user clicks 'submit' after filling details of new item
        if stockObj.write(name_entry.get(), 0, (r.get())
                          * float(minQty_entry.get())):
            messagebox.showinfo(
                "Success!!", "Item registered successfully in database", parent=raw)
        else:
            messagebox.showerror("Invalid data input!!!!!!!", parent=raw)

        name_entry.delete(0, END)
        minQty_entry.delete(0, END)

    Button(framei1_entry1, text="Quit",
           command=raw.quit).grid(row=5, column=0)

    Button(framei1_entry1, text="Submit",
           command=onsubmit).grid(row=5, column=1)


def additem():
    # add a new item(s)
    for widget in framei1_entry1.winfo_children():
        widget.destroy()

    results = stockObj.read()
    names = [result[0] for result in results]

    Label(framei1_entry1, text="Select the name of item : ").grid(row=0, column=0)
    a = StringVar()
    dropdown = OptionMenu(framei1_entry1, a, *names)
    dropdown.grid(row=0, column=1, ipadx=130)

    Label(framei1_entry1, text="Enter the qty of item added: ").grid(
        row=1, column=0)
    qtyEntry = Entry(framei1_entry1, width=50)
    qtyEntry.grid(row=1, column=1)

    re = IntVar()
    re.set("1")
    Radiobutton(framei1_entry1, text="Single multiplier",
                variable=re, value=1).grid(row=2, column=0, columnspan=2)
    Radiobutton(framei1_entry1, text="Dozen multiplier", variable=re,
                value=12).grid(row=3, column=0, columnspan=2)
    Radiobutton(framei1_entry1, text="Goods multiplier", variable=re,
                value=144).grid(row=4, column=0, columnspan=2)

    def onsubmit():
        try:
            qty = float(qtyEntry.get())
            qty = qty * float(re.get())
            name = a.get()
            existing = stockObj.read(name)
            if len(existing) == 1:
                existingObj = existing[0]
                if stockObj.update(name, actualQty=float(existingObj[1]) + qty):
                    messagebox.showinfo(
                        "Success!!", "Item updated successfully in database", parent=raw)
            else:
                print("Unique record not found for " + name)
                messagebox.showerror("Invalid data input!!!!!!!", parent=raw)
        except:
            messagebox.showerror("Invalid data input!!!!!!!", parent=raw)
        qtyEntry.delete(0, END)

    Button(framei1_entry1, text="Quit",
           command=raw.quit).grid(row=5, column=0)
    Button(framei1_entry1, text="Submit",
           command=onsubmit).grid(row=5, column=1)


def raw_material():
    # open Tkinter window for Raw materials management (create/add/etc.)
    
    global raw
    raw = Toplevel()
    raw.iconbitmap("Logo.ico")
    raw.geometry("610x400")
    raw.title("Raw Material Management")
    
    Label(raw, text="Raw Material Management", font=(
        "arial", 30)).grid(ipadx=80, row=0, column=0, columnspan=3)
    Button(raw, text="Create Item",
                        command=createitem, borderwidth=13).grid(row=2, column=0)
    Button(raw, text="Add Item", command=additem,
                        borderwidth=13).grid(row=2, column=1)
    
    global framei1_entry1
    framei1_entry1 = LabelFrame(
        raw, text="Raw material console", padx=10, pady=10)
    framei1_entry1.grid(row=3, column=0, columnspan=3)
    
    raw.mainloop()


l = Label(root, text="Jeet Sales Co.", font=("arial", 50)
          ).grid(ipadx=80, row=0, column=0, columnspan=3)

b1 = Button(root, text="Raw Material", command=raw_material,
            borderwidth=13).grid(row=2, column=0)

louis = ["YOU'VE COME TOO FAR TO QUIT.", "BE JHakass", 'Let them sleep while you grind. Let them party while you work. The difference will show.', "Our greatest fear should not be of failure, but of succeeding at things in life that don't really matter.", 'Money and success don’t change people; they merely amplify what is alr_labeleady there. – Will Smith ', 'Today you will work hard, you will study late night, you will skip parties, you will avoid hanging out with friends. But then tomorrow, you will enjoy your life in a much better way. Think about tomorrow, not today.', 'You can’t cheat the grind, it knows how much you have invested. It wont give you anything you haven’t worked for. ', "As Albert Einstein rightly said, The world won't be destroyed by those who do evil, but by those who watch them without doing anything.", 'A dream does not become reality through magic; it takes sweat, determination and hard work.', 'A year from now, we’ll see who was really working. ', 'Money and success don’t change people; they merely amplify what is alr_labeleady there. – Will Smith', 'You become strong by lifting others up, not pulling them down.', "Without God, you can do nothing. With God, there is nothing you can't do.", 'Talent is God given. Be humble. Fame is man-given. Be grateful. Conceit is self-given. Be careful. ', 'Once the game is over, the king and the pawn go back in the same box. -Italian Proverb', 'Being u matters', "Don't ever get to the point where you feel like I made it. Set new goals, keep learning and stay hungry.", "The real measure of our wealth is how much we'd be worth if we lost all our money", 'You don’t want to look back and know you could have done better', 'Live in the lead, but work hard like you’re trying to catch up.', 'Don’t worry about anything; instead pray about everything.', 'The tallest buildings start with a single brick. ', 'The greatest miracle of all is to be alive. Every morning you wake up, remember you have seen a miracle. ', 'Challenge yourself and find out precisely how good you are with words!', "Don't let people rush you with the timelines", 'Remember, when you are not training, someone somewhere is training; and when you meet him, he will win. ', "You're going to go through tough times - that's life. But I say, 'Nothing happens to you, it happens for you See the positive in negative events. – Joel Osteen ", "Everything happens when it needs to happen. But don't wait for extraordinary opportunities. Seize common occasions and make them great.", 'Don’t let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. – Earl Nightingale', "It isn't where you came from. It's where you're going that counts. – Ella Fitzgerald", "Don't be upset about the results you didn't get, from the work you didn't do.", 'If you’re confident about your strength, you don’t need to show me by putting somebody else down. Show me by lifting somebody else up. – BarackObama', "Do your little bit of good where you are; it's those little bits of good put together that overwhelm the world. – Desmond Tutu ", 'You can always be better', 'Courage doesn’t always roar. Sometimes courage isthe little voice at the end of the day that says I’ll try again tomorrow. —Mary Anne Radmacher', "The difference between a dreamer and a doer isn't luck, talent, skill or money. Unlike some dreamers who never get around to putting their dreams into action, doers make a promise to themselves to reach a goal and honor that commitment by taking determined action", "What you're supposed to do when you don't like a thing is change it. If you can't change it, change the way you think about it. Don't complain. –Maya Angelou", 'If youare building a house and a nail breaks, do you stop building or do you change the nail? — Rwandan proverb ', 'Don’t expect anyone to know your thoughts and feelings except yourself. Be brave enough to express and explain them to those worthy when needed.', "Just because something works doesn't mean it can't be improved. There's always room for improvement.", 'Before putting others in their place put yourself in their place.', 'If at first you don’t succeed, then skydiving definitely isn’t for you. – Steven Wright ', "Keep it moving, but don't mistake movement for progress. ", "Isn't it scary knowing that any time could be the last time you talk to someone? Always keep that in mind.", 'Be proud of yourself for how far you have come, and never stop pushing to be the best you can be.', "There's far more that you can perceive than only through the 5 human senses. –Deepak Chopra", 'Visualize yourself in the future as you want to be. Make that thought into a picture then step into the picture. Do this constantly',
         "Never forget how far you've come. Everything you have gotten through. All the times you have pushed on even when you felt you couldn't. All the mornings you got out of bed no matter how hard it was. All the times you wanted to give up but you got through another day. Keep going! ", "Don't be deceived by the spirit ofcomplacency and think you have achieved enough. Try to become better than you've been", "There may be peoplewho have more talent than you, but there's no excuse for anyone to work harder than you do - and I believe that", 'Never look down on anybody unless you’re helping them up. – Jesse Jackson', 'Never let an opportunity pass you by. Seize it with everything you have.', 'Don’t take someone else’s word on what you can accomplish', "When someone says you can't do it, do it twice and take pictures", "picture-perfect, you don't need no filter", 'If there be any truer measure of a man than by what he does, it must be by what he gives', 'if someone wants to be with you, nothing will stop them from doing so. Love doesn’t create excuses', 'People look at you and say you changed, as if you worked that hard to stay the same', 'Don’t be discouraged. It’s often the last key in the bunch that opens the lock', 'The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will. – Vince Lombardi Jr', 'Positive thinking can actually help increase your lifespan, strengthen your immune system and lower rates of depression', 'May you have every reason to raise your voice and your hands in praise. We hope every day of this month gives you a reason to smile and be happy. ', 'Shame is among the toughest, if not the toughest opponent we will ever face. It is never easy, ever. But because it’s so difficult, if we are brave enough to fight, the rewards it can yield can be life changing. Believe in you and never short change your value', 'It is impossible for a man to learn what he thinks he alr_labeleady knows.', 'THERE IS POWER IN KNOWING NOTHING!', 'The only thing worse than starting something and failing is not starting something.', '“The future starts today, not tomorrow.” – Pope John Paul II', 'Never discount the value of small acts and small gestures. Especially when it comes to kindness.', 'If you do tomorrow what you did today, you will get tomorrow what you got today. - Benjamin Franklin', 'Why don’t you focus on where you’re going and less on where you came from?', "Appreciate people for the little things. It feels good to be appreciated. It doesn't take much for you to show appreciation. You never know what someone is going through, sometimes a little encouragement from you is all it takes to give someone motivation to turn their life around. ", 'People look at you and say you changed, as if you worked that hard to stay the same. – Jay Z', 'If you admire someone, you should go ahead and tell them. People never get the flowers while they can still smell them.', 'The connections you have in your life should add value, not take value away. ', "There is only one person you spend your whole life with, and that is you. If you aren't ok with you, there is a problem.", 'The greatest man is not the one who never fell but rather the one who fell and was able to rise up again...it is possible to come out of anything!', 'There may be someone out there who has more talent than you, but there is no excuse for someone to work harder than you.', 'The past is a place of reference, not a place of residence; the past is a place of learning, not a place of living. –Roy T. Bennett', 'Loss of any kind is not easy. We feel some, if not all difficult emotions. Feel them, face them, don’t lock them up, but do so with a brave sense of accountability. All of us are tested now more than ever. Stay in touch and in tune with you, try to find lessons in any hardship. ', 'To the essential workers helping us all, to those that are struggling with the challenges these times bring mentally, physically, financially, and for those battling illness, this is for you', 'I wish nothing but the best for you', 'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing', 'No matter how good or bad you have it, wake up each day thankful for your life. Someone somewhere else is desperately fighting for theirs', 'A man who views the world the same at 50 as he did at 20 has wasted 30 years of his life. –Muhammad Ali ', "It doesn'tmatter how you look. As long as you train hard, you focus and you're hungry, and that drive is in you to follow your dreams, everything is possible", "Look inside of you and find that whisper", "MD Loves YOu Bro", "Be grateful", "Loss of any kind is not easy.We feel some,if not all difficult emotions.Feel them,don't lock them up,but do so with a brave sense of accountability", "Fu** the rest, u r the best", "Be satisfied -Preeti Jain"]

frame = LabelFrame(root, text="Thought of the day", padx=10, pady=10)
frame.grid(row=3, column=0, columnspan=3)
tde = datetime.datetime.today()
m = (int(tde.month))
d = (int(tde.day))
u = (m % 3)*30+d
ghee = louis[u]
lew = Label(frame, text=ghee).pack()


root.mainloop()
