---
title: "Installing MySQL and MySQL Workbench"
subtitle: "A step-by-step guide for Windows and Mac"
---

# Before You Start

You need to install **two separate programs**. They are not the same thing, and you need both.

| Program | What it is | Think of it like |
|---|---|---|
| **MySQL Server** | The actual database. It runs quietly in the background. It has no window and nothing to click. | The engine of a car |
| **MySQL Workbench** | The program you actually open and look at. You type your commands here and see results. | The steering wheel and dashboard |

**Important:** Installing only Workbench will not work. Workbench is just a window into the Server — with no Server installed, it has nothing to connect to.

## The exact files you need

Your instructor has specified these versions. If in doubt, match these.

**Windows**

| # | Product | File name |
|---|---|---|
| 1 | MySQL Community Server | `mysql-26.7.0-winx64.msi` |
| 2 | MySQL Workbench | `mysql-workbench-community-8.0.47-winx64.msi` |

**Mac** — the same two products, in the Mac equivalents that match your computer's chip (Part 2, Step 1 shows you how to check):

| # | Product | File name looks like |
|---|---|---|
| 1 | MySQL Community Server | `mysql-26.7.0-macos15-arm64.dmg` (or `-x86_64.dmg`) |
| 2 | MySQL Workbench | `mysql-workbench-community-8.0.47-macos-arm64.dmg` (or `-x86_64.dmg`) |

> **Why are the version numbers so different?** The Server is version **26.7.0** and Workbench is version **8.0.47**. That looks like a mistake, but it isn't — the two programs are numbered on separate schedules. They work together fine.
>
> One consequence: Workbench will show you a **warning about an "incompatible/nonstandard server version"** the first time you connect. **This is expected and harmless.** Part 3 tells you exactly what to click.

## What you need

- A laptop running **Windows 10 or 11**, or a **Mac**
- About **30–45 minutes**, mostly waiting for downloads
- A steady internet connection (the downloads are large — several hundred megabytes)
- Your computer's own login password (the installers will ask for permission to install)
- Somewhere safe to **write down one password you will create** (see the warning below)

## Read this before you do anything else

> ## ⚠️ THE #1 THING PEOPLE GET WRONG
>
> During setup you will be asked to **create a password for the "root" account**. This is a brand-new password that you make up on the spot. It is **not** your laptop password, not your school password, and not your email password.
>
> **Write it down immediately**, somewhere you will still have it in three months.
>
> If you forget this password, there is no "Forgot password?" link and no way to recover it. The only realistic fix is uninstalling and reinstalling everything from scratch.
>
> Suggestion: use something simple you will not lose, and keep it in your phone's notes app. For a class database on your own laptop, this does not need to be a fortress.

---

# Which MySQL Am I Supposed to Download?

The MySQL website offers a confusing number of products and versions. Here's how to cut through it.

## "Community" means the free one — that's the one you want

You will see the word **Community** on almost everything you download. That is correct and expected.

| Edition | Cost | Who it's for |
|---|---|---|
| **MySQL Community Edition** | **Free** | **You.** Students, hobbyists, most developers. Fully functional. |
| MySQL Enterprise Edition | Paid (thousands per year) | Large companies who want Oracle's phone support, monitoring tools, and auditing features |
| MySQL Standard / Cluster CGE | Paid | Big businesses running websites for millions of users |
| MySQL HeatWave | Paid, cloud-based | Companies running MySQL on Oracle's cloud instead of their own computers |

**The Community version is not a trial, not a demo, and not crippled.** It is the same database engine. The paid editions add support contracts and enterprise management tools you will never need for a class.

"MySQL Community" is also used as a **family name** for a group of free products released together:

- **MySQL Community Server** — the database itself ✅ *you need this*
- **MySQL Workbench** — the graphical design and administration tool ✅ *you need this*
- **MySQL Shell** — an advanced text-only command-line tool ❌ *not needed*
- **Connectors** (Connector/J, Connector/Python, Connector/NET) — plumbing that lets programs written in Java, Python, or C# talk to MySQL ❌ *not needed yet*

So when someone says "install MySQL Community," they mean: install the free edition — specifically the Server and Workbench.

If a download page mentions a **30-day trial** or asks for **billing information**, you are on the wrong page. Go back and look for *Community Downloads*.

## LTS vs. Innovation — two release tracks

MySQL publishes two kinds of releases at the same time. You'll see this on the download page's version dropdown.

| Track | Version looks like | What it means |
|---|---|---|
| **LTS** (Long-Term Support) | `9.7`, `8.4` | Stable. Gets security fixes for years but no new features. Companies use these. |
| **Innovation** | `26.7` (a date: July 2026) | The newest features, released every few months. Also stable — just moves faster. |

**What you should do:** unless your instructor named a specific version, **download whatever the page offers by default.** Both tracks work fine for coursework, and the SQL commands you'll learn are identical in all of them.

Don't worry if your version number doesn't match the ones in this guide. As long as it's version 8.0 or higher, you're fine.

## Other things on the download page you can ignore

The MySQL site lists a dozen products. For this course you need **exactly two**: *MySQL Community Server* and *MySQL Workbench*. Everything else — MySQL Router, MySQL Shell, Connector/J, Connector/Python, MySQL NDB Cluster — is for other purposes. Skip them.

---

# SQL, MySQL, Workbench, and "the Shell" — What's the Difference?

These four words get used interchangeably and it causes endless confusion. They are different things.

| Word | What it actually is |
|---|---|
| **SQL** | **A language**, like French or Python. You write instructions in it, such as `SELECT * FROM students;`. It's pronounced either "sequel" or "S-Q-L" — both are correct and people use both. |
| **MySQL** | **A program** that understands the SQL language and stores your data. It's one of many — others include PostgreSQL, SQLite, and Microsoft SQL Server. They all speak roughly the same SQL. |
| **MySQL Workbench** | **A window** for talking to MySQL, with buttons, menus, and a results table. This is what you'll use. |
| **A shell** (or *command line*, *terminal*, *Command Prompt*) | **A plain text window** for talking to MySQL. Same language, no buttons, no colors — you type a line, press Enter, and text comes back. |

## So what is a "shell," really?

A shell is just a window where you type commands instead of clicking things. On Windows it's called **Command Prompt** or **PowerShell**; on Mac it's called **Terminal**. It looks intimidating — black background, blinking cursor — but it's only a different way to give the same instructions.

You may also run across two MySQL-branded text windows:

- **MySQL Command Line Client** (Windows) — a shell that connects straight to your database
- **MySQL Shell** — a newer, fancier version of the same idea

**You do not need either one for this guide.** Workbench does everything they do, with a friendlier face. If your instructor later asks you to use one, that's a separate, short set of instructions.

> **The key insight:** the SQL you type is the *same* whether you type it in Workbench or in a shell. The shell is not "more advanced SQL" — it's just a plainer window. Don't let anyone make you feel behind for using Workbench.

## What SQL looks like

SQL reads almost like English. These are real, complete commands:

```
SELECT VERSION();

CREATE DATABASE my_class;

SELECT * FROM students WHERE grade > 80;
```

Three conventions worth knowing right now, because breaking them causes most beginner errors:

1. **Every command ends with a semicolon** `;` — forget it and MySQL will just sit there waiting, as if nothing happened.
2. **Capital letters are a style choice, not a rule.** `SELECT` and `select` both work. People write commands in capitals to make them stand out from names.
3. **Names are case-sensitive on Mac and Linux but usually not on Windows.** If `Students` doesn't work, try `students`.

---

# Part 1 — Windows

If you have a Mac, skip ahead to **Part 2**.

There are five steps. Do them in order.

## Step 1 — Install a required Microsoft component first

MySQL needs a small free Microsoft add-on called the **Visual C++ Redistributable**. Many computers already have it, but installing it again causes no harm and skipping it is the single most common cause of the error messages in the troubleshooting section.

1. Go to: **https://aka.ms/vs/17/release/vc_redist.x64.exe**
2. The file `vc_redist.x64.exe` downloads. Open it.
3. Tick **I agree to the license terms and conditions**, then click **Install**.
4. If it says it is already installed, click **Close**. You're fine.
5. Restart your computer if it asks you to.

## Step 2 — Download MySQL Server

1. Go to: **https://dev.mysql.com/downloads/mysql/**
2. Under **Select Operating System**, make sure it says **Microsoft Windows**.
3. You'll see a list of files. Find the one labeled **Windows (x86, 64-bit), MSI Installer** and click the blue **Download** button next to it.
    - It's the *smaller* of the choices, roughly 125 MB. The file name looks like `mysql-26.7.0-winx64.msi`.
    - Do **not** pick anything that says **ZIP Archive** or **Debug Binaries**.
4. The next page asks you to log in or sign up for an Oracle account. **You do not need an account.**
    - Scroll to the bottom and click the small link that says **"No thanks, just start my download."**
5. The download starts. Wait for it to finish before moving on.

## Step 3 — Install and set up MySQL Server

1. Open the file you just downloaded (check your **Downloads** folder).
2. If Windows shows a blue **"Windows protected your PC"** box, click **More info**, then **Run anyway**. This is normal — it appears because the file is new, not because anything is wrong.
3. Click **Next** through the installer, accept the license agreement, and click **Install**.
4. Click **Yes** when Windows asks for permission to make changes.
5. Wait. This takes a few minutes.
6. On the final screen, make sure the box to **run MySQL Configurator** is ticked, then click **Finish**.

A second program called **MySQL Configurator** now opens. This is where the real setup happens. Work through its screens:

**Type and Networking**

- Config Type: choose **Development Computer**
- Leave **TCP/IP** ticked and **Port** set to **3306**
- Click **Next**

**Authentication Method** (you may or may not see this screen)

- Leave the recommended option selected — the top one, about strong password encryption
- Click **Next**

**Accounts and Roles**

- This is the important one. Type your new password into **MySQL Root Password**, and type it again into **Repeat Password**.
- **Write this password down now.** See the warning on page 1.
- You do not need to add any other users. Click **Next**.

**Windows Service**

- Leave **Configure MySQL Server as a Windows Service** ticked
- Leave **Start the MySQL Server at System Startup** ticked — this makes the database turn on by itself every time you start your laptop, which is what you want
- Click **Next**

**Apply Configuration**

- Click **Execute**
- Wait for every line to get a green tick, then click **Finish**

MySQL Server is now installed and running in the background. You will not see a window for it. That's correct.

## Step 4 — Download and install MySQL Workbench

Workbench is a **separate download**. You are not done yet.

You need version **8.0.47** specifically. That is an older release, so it lives on the *Archives* page rather than the main download page.

1. Go to: **https://downloads.mysql.com/archives/workbench/**
2. In the **Product Version** dropdown, select **8.0.47**.
3. In the **Operating System** dropdown, select **Microsoft Windows**.
4. Click **Download** next to **Windows (x86, 64-bit), MSI Installer**. Confirm the file name is `mysql-workbench-community-8.0.47-winx64.msi` (about 255 MB).
5. On the next page, click **"No thanks, just start my download."** again.
6. Open the downloaded file.
6. Click **Next**, then **Next**, choose **Complete** if asked what type of install you want, then click **Install**.
7. Click **Finish**.

## Step 5 — Open Workbench and connect

1. Click the **Start** button and type `workbench`. Open **MySQL Workbench**.
2. On the home screen you should see a box labeled **Local instance MySQL** (or **Local instance MySQL80** / similar). Click it.
3. It asks for a password. Type the **root password you created in Step 3**.
4. Tick **Save password in vault** so you don't have to type it every time.
5. Click **OK**.

If a large window opens with a **Query 1** tab and a list of things on the left, **you are done.** Skip to **Part 3** to test it.

If you don't see a **Local instance** box, see *"Workbench opens but there's no connection listed"* in the troubleshooting section.

---

# Part 2 — Mac

If you have a Windows laptop, go back to **Part 1**.

There are five steps. Do them in order.

## Step 1 — Find out whether your Mac is ARM or x86

**Do not skip this.** Every Mac download comes in two flavors, and picking the wrong one is the most common Mac mistake. You'll need this answer **twice** — once for the Server, once for Workbench.

The two flavors:

- **ARM** — also written **arm64** or **Apple Silicon**. Macs with Apple's own M1/M2/M3/M4 chips.
- **x86** — also written **x86_64**, **Intel**, or sometimes just **64-bit**. Older Macs with Intel chips.

### Method 1: About This Mac (easiest)

1. Click the **Apple menu** (the apple icon) in the very top-left corner of your screen.
2. Click **About This Mac**.
3. Look for a line labeled **Chip** or **Processor**:

| What that line says | Your Mac is | Download the file marked |
|---|---|---|
| **Apple M1 / M2 / M3 / M4** — any "Apple M" number, with or without Pro, Max, or Ultra | **ARM** / Apple Silicon | **ARM, 64-bit** or `arm64` |
| **Intel Core i3 / i5 / i7 / i9**, or **Intel Xeon** | **x86** / Intel | **x86, 64-bit** or `x86_64` |

The rule is simple: **if you see the word "Apple," you're ARM. If you see the word "Intel," you're x86.**

### Method 2: Ask the Mac directly (if Method 1 was unclear)

1. Press **⌘ + Space**, type `Terminal`, and press **Enter**. A plain text window opens — this is a "shell," as described earlier in this guide.
2. Type this exactly, then press **Enter**:

```
uname -m
```

3. Read the one-word answer:

| It prints | Your Mac is |
|---|---|
| `arm64` | **ARM** / Apple Silicon |
| `x86_64` | **x86** / Intel |

4. Close the Terminal window. You're finished with it.

### Rough guide by age

Can't check right now? Macs sold from **late 2020 onwards** are almost all Apple Silicon (ARM). Macs from **2019 and earlier** are Intel (x86). Use this only as a sanity check — always confirm with Method 1 or 2 before downloading.

> ✍️ **Write your answer down before continuing:** my Mac is **ARM** / **x86** (circle one)

### What if I download the wrong one?

Nothing breaks permanently.

- On an **ARM** Mac, an x86 version will usually still run — macOS quietly translates it, sometimes after asking to install something called **Rosetta**. It just runs slower.
- On an **Intel** Mac, an ARM version **will not run at all**. You'll often get a misleading message saying the app is "damaged."

Either way the fix is the same: delete it and download the other one.

## Step 2 — Download MySQL Server

1. Go to: **https://dev.mysql.com/downloads/mysql/**
2. Under **Select Operating System**, choose **macOS**.
3. You'll see a list of files. Find the one that:
    - matches your chip from Step 1 (**ARM, 64-bit** or **x86, 64-bit**), and
    - says **DMG Archive**
    - The file name looks something like `mysql-26.7.0-macos15-arm64.dmg`
4. Click the blue **Download** button next to it.
5. The next page asks you to log in or sign up for an Oracle account. **You do not need an account.** Scroll to the bottom and click **"No thanks, just start my download."**
6. Wait for the download to finish.

> **Not sure which one to pick?** If the list shows a macOS version number higher than yours (for example it says macOS 15 and you have macOS 14), that's usually still fine. Pick the closest one that matches your chip.

## Step 3 — Install MySQL Server

1. Open your **Downloads** folder and double-click the `.dmg` file. A small window opens.
2. Inside it is a file ending in **`.pkg`**. Double-click that.
3. If macOS blocks it and says it's from an **unidentified developer**, do this:
    - Open the **Apple menu** → **System Settings** → **Privacy & Security**
    - Scroll down to the **Security** section
    - You'll see a message about the blocked file, with an **Open Anyway** button. Click it.
    - Enter your Mac password, then try the `.pkg` again.
4. Click **Continue** through the screens, then **Agree** to the license, then **Install**.
5. Enter **your Mac login password** when asked. (This one is your normal Mac password — the MySQL password comes next.)
6. A **Configuration** screen appears:
    - Leave the recommended password-encryption option selected (the top one) and click **Next**
    - Now type a **root password** and confirm it. **This is the new password you make up. Write it down now.** See the warning on page 1.
    - Leave **Start MySQL Server once the installation is complete** ticked
    - Click **Finish**
7. When it says the installation was successful, click **Close**. You can click **Move to Trash** if it offers.

## Step 4 — Check that the Server is running

1. Open the **Apple menu** → **System Settings**.
2. Scroll all the way down the left-hand list. At the very bottom you'll find **MySQL**. Click it.
3. It should say the **MySQL Server Instance is running**. 

If it says *stopped*, click **Start MySQL Server** and enter your Mac password.

This is also where you come back later if the database ever seems to be off.

## Step 5 — Download and install MySQL Workbench

Workbench is a **separate download**. You are not done yet.

You need version **8.0.47** specifically. That's an older release, so it lives on the *Archives* page rather than the main download page.

1. Go to: **https://downloads.mysql.com/archives/workbench/**
2. In the **Product Version** dropdown, select **8.0.47**.
3. In the **Operating System** dropdown, select **macOS**.
4. Pick the file that matches your chip from Step 1 — **ARM, 64-bit** for Apple Silicon, **x86, 64-bit** for Intel. Click **Download**.
5. Click **"No thanks, just start my download."**
6. Open the downloaded `.dmg` file. A window opens showing the **MySQLWorkbench** icon and a shortcut to your **Applications** folder.
6. **Drag the MySQLWorkbench icon onto the Applications folder.** That is the installation — there's nothing else to click.
7. Close the window. Right-click the disk image on your desktop or in Finder's sidebar and choose **Eject**.

## Step 6 — Open Workbench and connect

1. Open **Launchpad** (or your **Applications** folder) and click **MySQLWorkbench**.
2. The first time, macOS may warn that it was downloaded from the internet. Click **Open**.
    - If it refuses entirely, use the **Apple menu** → **System Settings** → **Privacy & Security** → **Open Anyway** trick from Step 3.
3. On the home screen, look for a box labeled **Local instance 3306**. Click it and enter your **root password**.

**If there is no such box**, create the connection yourself — it takes ten seconds:

1. Click the **+** next to **MySQL Connections**.
2. Fill in exactly this:
    - **Connection Name:** `Local`
    - **Hostname:** `127.0.0.1`
    - **Port:** `3306`
    - **Username:** `root`
3. Click **OK**, then click your new **Local** box and enter your root password.

If a large window opens with a **Query 1** tab, **you are done.** Continue to Part 3.

> **You may see a yellow warning** saying *"Could not acquire management access for administration."* You can ignore this completely. It only affects buttons you won't use in this course.

---

# Part 3 — Make Sure It Actually Works

## First: the warning you are expected to see

The very first time you connect, Workbench will almost certainly pop up a box like this:

> **Connection Warning**
> Incompatible/nonstandard server version or connection protocol detected (26.7.0).
> A connection to this database can be established but some MySQL Workbench features may not work properly since the database is not fully compatible with the supported versions of MySQL.

**This is expected. Nothing is wrong. Nothing is broken or unsafe.**

Workbench 8.0.47 was built and tested against older MySQL Servers, so when it meets Server 26.7.0 it politely warns you that it's newer than it recognizes. Everything you'll do in this course — writing queries, creating tables, viewing results — works normally.

**What to do:** tick **Don't show this message again**, then click **Continue Anyway**.

## Now test it

Do this on both Windows and Mac. It takes one minute and proves everything is installed correctly.

1. In MySQL Workbench, click into the large white box in the middle of the screen (the tab labeled **Query 1**).
2. Type exactly this, including the semicolon:

```
SELECT VERSION();
```

3. Click the **lightning bolt** icon (⚡) above the box. Or press **Ctrl + Enter** on Windows, **⌘ + Enter** on Mac.
4. A **Result Grid** appears at the bottom showing a version number, such as `26.7.0`.

**If you see a version number, your installation is complete and working.** Congratulations.

## Optional: create your first database

Still in the same box, delete what you typed and enter:

```
CREATE DATABASE test_db;
```

Run it with the lightning bolt. Then look at the **Schemas** panel on the left side and click the small refresh arrow (⟳). You should now see **test_db** in the list.

("Schema" is just MySQL's word for a database. You'll see both words used to mean the same thing.)

To delete it again when you're finished experimenting:

```
DROP DATABASE test_db;
```

---

# Part 4 — When Something Goes Wrong

**Something going wrong is normal.** Installing a database is one of the fussiest things people do on a laptop, and experienced programmers hit these same errors. Nothing here means you broke your computer or that you're bad at this.

## Before you panic: the five things to try first

Work down this list. It resolves the large majority of problems, and none of it can do any harm.

1. **Read the error message all the way through.** It usually says exactly what's wrong in plain-ish English. See *How to read an error message* below.
2. **Close the program completely and open it again.** Not minimize — quit it. (Windows: the ✕ button. Mac: **⌘ + Q**, because closing the window doesn't quit a Mac app.)
3. **Restart your laptop.** Genuinely. Half-finished installs are extremely common and a restart clears them.
4. **Check the Server is actually running** — see *"Can't connect to MySQL server"* below. An enormous share of "Workbench is broken" reports are just the Server being switched off.
5. **Try the step again from the beginning.** Re-running an installer is safe. It will not duplicate anything or corrupt what's there.

If all five fail, go to the specific error lists further down.

## How to read an error message

Error messages look like noise, but they follow a pattern. Take this one:

```
Can't connect to MySQL server on '127.0.0.1' (10061)
```

- **`Can't connect to MySQL server`** — the plain-English part. *This* is the actual problem. Read this bit first, and ignore everything else on the first pass.
- **`'127.0.0.1'`** — where it tried to look (your own computer)
- **`(10061)`** — an error number. Useless to you, useful for searching.

Two habits that will serve you for the rest of your degree:

- **Read the first line, not the last.** Long errors pile up consequences underneath the real cause. The top line is usually the one that matters.
- **Copy the message and search it.** Paste the exact text into Google, minus anything personal like your username or file path. Thousands of people have hit the identical error. Results from **stackoverflow.com** and **dev.mysql.com** are usually the reliable ones.

## How to take a screenshot (for asking for help)

A photo of the error gets you help ten times faster than describing it.

- **Windows:** press **Windows key + Shift + S**, drag a box around the error, then paste into your email or message with **Ctrl + V**.
- **Mac:** press **⌘ + Shift + 4**, drag a box around the error. The image saves to your Desktop.

Capture the **whole window**, not just the red text — the surrounding context is often what identifies the problem.

## Problems that happen before you even get installed

**The download is extremely slow, stalls, or fails partway**

The files are large and Oracle's servers are sometimes slow. Let it run, and don't put the laptop to sleep while it downloads. If it dies partway, delete the partial file and start the download over — a half-downloaded installer produces confusing errors later.

**Campus Wi-Fi or a VPN is blocking the download**

Some school networks block large downloads or certain sites. Try again on home Wi-Fi or a phone hotspot, or disconnect your VPN first.

**"You need administrator privileges" / the installer won't run**

You need to be on an account that's allowed to install software. On a personal laptop you usually are. On a **school- or work-issued laptop**, you may be locked out by IT — that's not something you can fix yourself, and you should contact your IT help desk or your instructor rather than fighting it.

**Not enough disk space**

MySQL Server plus Workbench need roughly **3 GB** free, more during installation. Empty your Trash/Recycle Bin and clear your Downloads folder if you're tight on space.

**Antivirus software blocks or quarantines the installer**

Some antivirus programs flag database installers because they open a network port. If your antivirus removes the file, re-download it from **dev.mysql.com only** and, if needed, pause your antivirus for the few minutes the install takes — then turn it back on.

**My Mac says the app requires a newer version of macOS**

Your Mac is older than the version MySQL was built for. Go to the download page, click the **Archives** link, and pick a slightly older MySQL release. Bring this to your instructor if you get stuck — older Macs sometimes need a specific pairing.

## Both Windows and Mac

**"Access denied for user 'root'@'localhost'"**

The password is wrong. This almost always means you're typing your laptop password instead of the root password you created during setup. Try again carefully.

If you truly can't remember it, see *"I forgot my root password"* below.

**"Can't connect to MySQL server on '127.0.0.1'"** or **error 2003 / 10061**

Workbench is running, but the Server isn't. Workbench alone can't do anything.

- **Windows:** press the **Start** button, type `services`, open **Services**. Find **MySQL** in the list, right-click it, choose **Start**.
- **Mac:** **Apple menu** → **System Settings** → scroll to the bottom → **MySQL** → **Start MySQL Server**.

If there's no MySQL entry at all, the Server never got installed. Go back and do Part 1 Steps 2–3 (or Part 2 Steps 2–3).

**"Incompatible/nonstandard server version or connection protocol detected"**

Expected and harmless — Workbench 8.0.47 is older than Server 26.7.0 and says so. Tick **Don't show this message again** and click **Continue Anyway**. See Part 3 for the full explanation.

**I can't find Workbench 8.0.47 on the download page**

The main download page only offers the newest release. Version 8.0.47 is an older one, so it's on the **Archives** page instead: **https://downloads.mysql.com/archives/workbench/** — then choose **8.0.47** in the *Product Version* dropdown.

**The download page keeps asking me to make an Oracle account**

You don't need one. Scroll to the very bottom of that page and click the small link **"No thanks, just start my download."**

**I forgot my root password**

There is no recovery option. For a fresh class setup, the fastest fix by far is to uninstall MySQL Server and reinstall it, choosing a new password and writing it down this time.

- **Windows:** Start → **Add or remove programs** → uninstall everything starting with **MySQL** → then redo Part 1.
- **Mac:** **Apple menu** → **System Settings** → **MySQL** → **Uninstall**, then redo Part 2.

You will lose any databases you created. If you've already done real coursework in there, talk to your instructor before uninstalling — there are recovery methods, but they're fiddly and worth doing with help.

**Port 3306 is already in use**

Something else on your computer is already running a database — usually XAMPP, WAMP, Docker, or an older MySQL. Close or uninstall that program, then try again. If you need both, ask your instructor; using a different port is possible but changes the connection settings.

## Windows only

**"VCRUNTIME140_1.dll was not found"** or **"MSVCP140.dll is missing"**

You skipped Step 1. Install the Visual C++ Redistributable from **https://aka.ms/vs/17/release/vc_redist.x64.exe**, restart, and try again.

**Workbench installs but won't open, or flashes and closes**

Same cause as above nine times out of ten. Install the Visual C++ Redistributable, restart your computer, and try again.

**"Windows protected your PC" blue box**

Click **More info**, then **Run anyway**. This appears for most newly downloaded installers and does not mean the file is unsafe.

**Workbench opens but there's no connection listed**

Create one manually: click the **+** next to **MySQL Connections** and enter Connection Name `Local`, Hostname `127.0.0.1`, Port `3306`, Username `root`. Click **OK**.

## Mac only

**"MySQLWorkbench cannot be opened because the developer cannot be verified"**

**Apple menu** → **System Settings** → **Privacy & Security** → scroll to the **Security** section → click **Open Anyway** next to the message about MySQLWorkbench → enter your Mac password.

**"MySQLWorkbench is damaged and can't be opened"**

This usually means the download was interrupted, or you downloaded the wrong chip version. Delete it, re-check your chip (Part 2, Step 1), and download again.

**Workbench looks blurry or sluggish**

You installed the Intel version on an Apple Silicon Mac. It still works, but delete it and download the **ARM, 64-bit** version for better results.

**Yellow banner: "Could not acquire management access for administration"**

Harmless. Ignore it. Writing and running queries works normally.

---

# Part 5 — Using It Day to Day

**You do not need to reinstall anything ever again.** After setup, this is your routine:

1. Open **MySQL Workbench**
2. Click your connection (**Local instance** / **Local**)
3. Type your commands and click the lightning bolt (⚡)

**Does the database need to be turned on first?** Normally no — it's set to start automatically when your laptop starts. If you get a connection error, turn it on using the instructions under *"Can't connect to MySQL server"* above.

**Should I turn it off when I'm not using it?** No need. It uses very little of your computer's resources sitting idle.

**Do I close Workbench or the Server when I'm done?** Just close Workbench like any other app. Leave the Server alone.

---

# Quick Glossary

| Term | What it means |
|---|---|
| **MySQL Server** | The database itself. Runs invisibly in the background. |
| **MySQL Workbench** | The app you open to type commands and see results. |
| **root** | The main administrator username for your database. You'll use this for the whole course. |
| **localhost** / **127.0.0.1** | "This computer." Your database lives on your own laptop, not the internet. |
| **Port 3306** | The doorway Workbench uses to talk to the Server. Always leave it as 3306. |
| **Schema** | Another word for a database. MySQL uses both words interchangeably. |
| **Query** | A command you write, like `SELECT VERSION();`. |
| **Result Grid** | The table of results that appears at the bottom after you run a query. |

---

# Final Checklist

Before your next class, confirm all of these:

- [ ] MySQL **Server** is installed
- [ ] MySQL **Workbench** is installed
- [ ] My root password is **written down somewhere I won't lose it**
- [ ] Workbench opens and I can click into my connection without an error
- [ ] Running `SELECT VERSION();` gives me a version number

## If you're still stuck

Bring your laptop to office hours or lab, and be ready to say:

1. **Windows or Mac**, and which version
2. **Which step** you got to before it went wrong
3. **The exact error message** — a photo or screenshot is perfect

Nearly every problem is one of the five things in the troubleshooting section, and all of them are quick to fix in person. Don't spend hours on it alone.
