# 42_EXAM SIMULATION 

⚠️ Important Notice

Some exercises have been intentionally removed from this fork to better reflect current exam expectations and to improve overall quality and maintenance.
This does not affect the core functionality of the simulator or its usefulness for exam preparation.

#### Disclaimer: This project is a "fork" of the 42_exam from [JCluzet](https://github.com/JCluzet), all credits for this project go to them. This fork aims to provide knowledge freely and open source.

# Requirements

To run this project, you need to have the `readline` library installed. If it's already installed on your system, you can skip these steps. Otherwise, follow the instructions below based on your Linux distribution.

## For Debian-based distros (e.g., Ubuntu, Kali, etc.):

```bash
sudo apt update && sudo apt install libreadline-dev
```

## For Red Hat-based distros (e.g., Fedora, CentOS, etc.):

```bash
sudo dnf update && sudo dnf install readline-devel ncurses-devel
```
# Start  
```
git clone https://github.com/orgito1015/Grademe-edu && cd Grademe-edu && make && make
```
Or  
```
source <(curl https://raw.githubusercontent.com/orgito1015/Grademe-edu/main/install.sh)
```

## Practice for the 42 exams 🏊‍♂️

- [x] New subjects ExamRank02  
- [x] Randomized subjects  
- [x] Wait time for correction  
- [x] Time limit  
- [x] Automatic correction (even without internet)  
- [x] Traceback available  
- [x] Detects infinite loop in your program (ExamRank02)  
- [x] **Clear exercise descriptions** for all 138 exercises
- [ ] Detects infinite loop across all Grademe  
- [ ] Detects leaks in all exercises

## Exercise Descriptions

Every exercise in this simulator now includes a comprehensive README.md file with:
- Clear description of what the program must do
- Expected input/output specifications
- Allowed functions and constraints
- Example usage demonstrating expected behavior

You can find the description for any exercise in its directory:
```
.subjects/PISCINE_PART/exam_XX/[level]/[exercise_name]/README.md
.subjects/STUD_PART/exam_XX/[level]/[exercise_name]/README.md
```

For example:
```bash
# View description for aff_a exercise
cat .subjects/PISCINE_PART/exam_01/0/aff_a/README.md

# View description for ft_printf exercise
cat .subjects/STUD_PART/exam_03/0/ft_printf/README.md
```  

# 👓 CHEAT code:  

**remove_grade_time**: removes the wait time between "grademe"  
**force_success**: forces a success on the exercise  
**new_ex**: generates a new random exercise  

You can contribute by adding a new exercise or improving the program.  

**gradenow**: Correction without wait time  

#  GDPR:  
NO personal information is collected during the exam.

# Disclaimer:

This project is a "fork" of the 42_exam from [JCluzet](https://github.com/JCluzet), all credits for this project go to them.  
This fork aims to provide knowledge freely and open source, bringing improvements focused on the campuses,  
with the purpose of helping students understand their mistakes and improve with them.  
Grademe is and will always be a non-profit tool with purely educational purposes.

# Your help is very welcome

👋 If you have any issues with a test, create an "Issue" here on GitHub. It will only take 3 minutes of your time and will be a great help to the community. 
