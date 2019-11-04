# Applied Statistics 2019 - Code Repository

This git is a repository of the code that will be used in the Applied Statistics code 2019 edition.


## Getting Started

The following instructions will help you install the relevant software that will be used in the course.

Note that you have two options for installing and running the applied statistics notebooks. The first option involves running the code on [ERDA](https://erda.ku.dk), a KU-based server platform that has the advantage of having a uniform software environment for everyone. If you are not enrolled as a KU student, you should contact [Troels](mailto:petersen@nbi.dk) to get access to the ERDA servers. The second option is to install everything on your laptop, using the anaconda environment as a standard set of python libraries. 

We highly recommend that you use __BOTH__ methods throughout the course. Having a local copy of the exercices can become very handy when the ERDA servers are down (for maintenance or other reasons).

### Option A. Running things on ERDA
---

#### Get Registered on ERDA (email [Troels](mailto:petersen@nbi.dk) to get registered)

#### [Get a github account](https://github.com/). 

If you do not wish to do so, you can still access the course content by manually downloading the repository (see __Option C__ below)

#### Clone the Applied Statistics Repository


<details><summary>From your ERDA homepage, click on the <b>jupyter</b> option in the side menu</summary>
<img src="/images/ERDA_step1.png"
	title="ERDA main menu"/>
</details>


<details><summary>Start a terminal session by clicking the <b>Start DAG</b> button</summary>
<img src="/images/ERDA_step2.png"
	title="ERDA main menu"/>
</details>



<details><summary>To spawn the correct environment for the course, select the option <b>Statistics Notebook with Python</b> </summary>
<img src="/images/ERDA_step3.png"
	title="ERDA main menu"/>
</details>



<details><summary>Open the <b>Terminal</b> option </summary>
<img src="/images/ERDA_step4.png"
	title="ERDA main menu"/>
</details>


You should now have a terminal window opened in your screen. If you type in the command `ll`, you should see a list of folder in your space. Move into the __work__ folder by typing the command `cd work`.

<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_step5.png"
	title="ERDA main menu"/>
</details>


Once you are in your __work__ folder, make yourself a local copy of the code repository by typing the command `git clone https://github.com/AppliedStatisticsNBI/AppStat2019.git ./AppStat2019_local/`. If you list the content of your __work__ directory, you should now see a local copy of the code appear on your machine.

<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_step6.png"
	title="ERDA main menu"/>
</details>



### Option B. Running things on your laptop
---

Given the wide range of operating systems available out there, we cannot guarantee that the instructions above will work on _all_ platforms. As of now, __the instructions below have been tested on the following systems:__

* [__Instructions for Linux__](./docs/install_instruction_linux.md)

* [__Instructions for Windows 10__](./docs/install_instruction_windows10.md)

* [__Instructions for MacOs Mojave__](./docs/install_instruction_macos_mojave.md)


### Option C. Manually downloading the course content
---

If you do not want to subscribe to github, you can still download manually the content of the repository using the __donwload zip__ option on the main page of this git. 

<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_zip0.png"/>
</details>


To upload the archive on ERDA, go to your main page, on the __Files__ section and right click on the window on the right side. Select the __upload__ button
<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_zip1.png"/>
</details>


Type in a folder name in __Optional final destination dir__ if you want to save it in a folder other than your home diretory. Start the upload by clicking on the __Start__ button.
<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_zip2.png"/>
</details>


You should now see the zip archive in the folder you saved it to. To unzip the archive, right click on it and select the __unpack__ option.
<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_zip3.png"/>
</details>



Enter a path name for where you want to have your unzipped archive (optional). Click on __Ok__. Your folder is now unpacked and you should be able to work in it
<details><summary>Click here to see the image</summary>
<img src="/images/ERDA_zip4.png"/>
</details>



__Important note regarding a manual download:__ If you choose this method to get the course content, you will have to download a new version of the archive everytime we update an exercice or correct a mistake in the notebooks. __It is therefore highly recommended that you use github instead.__ 


---

## Link to Course Information

*	[Course Main page](https://www.nbi.dk/~petersen/Teaching/AppliedStatistics2019.html)
