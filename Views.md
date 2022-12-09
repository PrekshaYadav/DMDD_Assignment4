# Views for Use-Cases Implemented:-

## Assignment 3 Use-Cases:

Select * from Standards;

Select * from Requirements;

Select * from University;


1.  Top 5 USA universities.

        Create View TopFiveUni As Select University_name from University Where Country = "USA" order by National_Rank asc limit 5;
    
    `Select * from TopFiveUni;`
    <img width="186" alt="v1" src="https://user-images.githubusercontent.com/113796019/206624989-9426a8e6-82c2-465b-9a4f-35f25c936245.png">

2.  Top 5 universities that provides best education.

        Create View BestEdu As select university.university_name, standards.Quality_of_Education from University left join Standards on university.university_ID = standards.university_ID order by standards.quality_of_education limit 5;

    `Select * from BestEdu;`
    <img width="260" alt="v2" src="https://user-images.githubusercontent.com/113796019/206625048-f413836f-0239-4a0d-9a88-65c0e2f8c142.png">

3.  Top 10 ambitious institutes.

        Create View AmbitiousInstitute As Select University_ID, University_name, Chance_of_admit from university order by chance_of_Admit limit 10;

    `Select * from AmbitiousInstitute;`
    <img width="303" alt="v3" src="https://user-images.githubusercontent.com/113796019/206625083-be3de32a-f931-410e-8fbc-69465a50d9e3.png">

4.  Rate the university based of quality of faculty.

        Create View UniversityRating_Qof As Select university.University_Id, university.University_name, standards.Quality_of_Faculty from University left join Standards on University.University_ID = Standards.University_ID order by Quality_of_Faculty;

    `Select * from UniversityRating_Qof;`
    <img width="320" alt="v4" src="https://user-images.githubusercontent.com/113796019/206625139-ea366148-3d68-4776-b7b3-d18585653f5c.png">

5.  Count the number of universities with distinct university ratings.

        Create View DistinctUniRating As Select University_rating, Count(University_Name) as No_of_Universities from university group by University_rating order by University_rating;

    `Select * from DistinctUniRating;`
    <img width="182" alt="v5" src="https://user-images.githubusercontent.com/113796019/206625163-aee423fe-6b16-4d04-ba7e-f8992a65bcb3.png">

6.  Universities that does not require research

        Create View UniWithoutRearch As Select University_name from University left join requirements on University.University_ID = Requirements.University_ID where research = 0;

    `Select * from UniWithoutRearch;`
    <img width="208" alt="v6" src="https://user-images.githubusercontent.com/113796019/206625196-5d36d575-1006-47d8-9887-a1846aef7ddb.png">

7.  Universities that are best fit for a student with GRE score 315 and TOEFL score 110.

        Create View BestFit As Select University.University_Id, University_Name, GRE, TOEFL from University left join Requirements On University.University_Id = Requirements.University_Id where GRE between 310 and 316 AND TOEFL between 105 and 112;

    `Select * from BestFit;`
    <img width="323" alt="v7" src="https://user-images.githubusercontent.com/113796019/206625227-600da2e9-148e-47a0-bafd-9ad8c2b73f30.png">

8.  Should a student with GRE score "321" apply to Northeastern University?

        Create View NEU_GRE As select University_name, GRE, case when GRE < 321 then 'YES' else 'NO' End as Decision From University left join requirements on University.University_ID = Requirements.University_ID where University_name = 'Northeastern University';

    `Select * from NEU_GRE;`
    <img width="217" alt="v8" src="https://user-images.githubusercontent.com/113796019/206625268-bb04fa80-3190-462b-b391-1122bcfa78a9.png">

9.  What are the pre requisites to apply to Northeastern University?

        Create View PreReq_NEU As Select University.University_ID, University_name, academic_year, score, gre, toefl, sop, lor, cgpa, research from University right join Requirements on University.University_ID = requirements.University_ID where University_name = 'Northeastern University';

    `Select * from PreReq_NEU;`
    <img width="479" alt="v9" src="https://user-images.githubusercontent.com/113796019/206625302-6a42c0f6-6856-46fc-9383-c36f763fc33f.png">

10. Number of students employed from university of Oklahoma.

        Create View UOO As Select University.University_ID, University_name, Alumni_Employement from University inner join Standards on standards.University_ID = University.University_ID where University_name = 'University of Oklahoma - Norman Campus';

    `Select * from UOO;`
    <img width="346" alt="v10" src="https://user-images.githubusercontent.com/113796019/206625331-e4af7456-4b7d-4fb5-aa6c-39df36aad16d.png">

11. What is the basic GPA requirement and chance of getting admit at 'University of Pennsylvania'?

        Create View UOP As Select University_Name, CGPA from Requirements left join University on Requirements.university_id = University.university_id where university_name = 'University of Pennsylvania';

    `Select * from UOP;`
    <img width="164" alt="v11" src="https://user-images.githubusercontent.com/113796019/206625377-1d546f9d-5a7a-4744-ab9d-c43a9e084346.png">
    
12. What is the university_rating and national_rank of Cornell University?

        Create View CURanking As Select University_name, University_rating, national_rank from University where University_Name = 'Cornell University';

    `Select * from CURanking;`
    <img width="248" alt="v12" src="https://user-images.githubusercontent.com/113796019/206625424-aeea30ee-64ea-4735-9920-e7fb45525d28.png">    

13. Which university has highest GRE and GPA requirements?

        Create View Highest_GRE_GPA As Select university_name , min(CGPA) , min(GRE) from University left join Requirements on  University.university_id = Requirements.university_id;

    `Select * from Highest_GRE_GPA;`
    <img width="220" alt="v13" src="https://user-images.githubusercontent.com/113796019/206625454-af40fb8c-a6f6-4357-97a7-fff374660471.png">

14. University with highest alumni employment and publications?

        Create View Highest_Alumni_Emp As Select university_name, max(alumni_Employement) from University left join Standards on University.university_id = Standards.university_id;

    `Select * from Highest_Alumni_Emp;`
    <img width="223" alt="v14" src="https://user-images.githubusercontent.com/113796019/206625476-4517aa3c-28a3-4256-b393-da298d0f958e.png">

15. View the university with lowest score in the year 2012.

        Create View Uni_with_lowest_score As Select University_name, min(score) from University left join requirements on University.University_ID = Requirements.University_ID where academic_year = '2012';

    `Select * from Uni_with_lowest_score;`
    <img width="271" alt="v15" src="https://user-images.githubusercontent.com/113796019/206625537-b08f6ba4-2c0b-4757-81ba-2b969772becf.png">

## Previous use cases:-

## Shreyasi:

1.  What is the tuition Fees of a particular course?

    The dataset does not have a details of tuition fees.

2.  What are the admission requirements of a course?

    We have admission requirements of a particular university but since there are no course detials we cannot fetch the requirements os a specific course

        Create View UniAdmissionReq As Select University.university_ID, University_name, Score, GRE, TOEFL, SOP, LOR, CGPA from university right join requirements on University.university_Id = Requirements.University_ID;

    `Select * from UniAdmissionReq;`
    <img width="468" alt="s2" src="https://user-images.githubusercontent.com/113796019/206625608-64f9397b-5f0b-4af2-9052-8c2d876a8293.png">

3.  What is the course structure? 

    The dataset does not have a details of course structure.

4.  Which universities have waived of GRE score?

    All the universities in the dataset have specific GRE score requirement

5.  Top universities for GRE score less than 320? 

        Create View UniGREScore As Select University.university_ID, University_name, GRE from university right join requirements on University.university_Id = Requirements.University_ID where GRE < 320;

    `Select * from UniGREScore;`
    <img width="284" alt="s5" src="https://user-images.githubusercontent.com/113796019/206625650-94b8d320-36c6-4ca7-8b74-9a99cb26300d.png">

6.  What are the total number of international students registered in the university? 

    No such information present in the dataset

7.  Number of courses available in the university? 

    The dataset does not have a details of courses.

8.  What is the course duration? 

    The dataset does not have a details of courses.

9.  What is the campus location? 

        Create View UniCampLoc As Select University_Name, Country from University;

    `Select * from UniCampLoc;`
    <img width="218" alt="s9" src="https://user-images.githubusercontent.com/113796019/206625699-fb38feb0-fcc0-4285-b1b5-31c1ce07d9c2.png">

10. How much is the application fees?

    Application fees details not available in the dataset


## Preksha:

1.  What are the top 10 universities for a particular course? 

    Database does not have details of course name .

2.  What are the top 3 universities in a state? 

    Database does not have a state name.

3.  What is the acceptance rate of the university ? 

        Create View UniAccRate As Select university_name, chance_of_admit from university where university_name = 'Northeastern University';

    `Select * from UniAccRate;`
    <img width="218" alt="p3" src="https://user-images.githubusercontent.com/113796019/206625745-b1b244cd-209c-4250-9950-28d1f876e77d.png">    

4.  What is the placement rate of the university ? 

        Create View UniPlacementRate As Select university_name, alumni_employement from University left join Standards on University.university_id = Standards.university_id;

    `Select * from UniPlacementRate;`
    <img width="266" alt="p4" src="https://user-images.githubusercontent.com/113796019/206625781-fc1cabc1-61b3-4b6e-89ba-a220a4b01f66.png">

5.  What is the financial aid of the university?

    Database does not have a financial  aid

6.  What are the top universities for TOEFL scores less than 100? 

        Create View UniTopTOEFL As Select university_name, TOEFL, national_rank from University left join Requirements on University.university_id = Requirements.university_id order by national_rank;

    `Select * from UniTopTOEFL;`
    <img width="275" alt="p6" src="https://user-images.githubusercontent.com/113796019/206625828-8e477291-ac75-4cce-919e-ca2588ff91f4.png">

7.  What is the minimum score required in GRE, TOEFL . 

        Create View GRETOEFL_MinScore As Select university_name, min(GRE), min(TOEFL) from University left join Requirements on University.university_id = Requirements.university_id;

    `Select * from GRETOEFL_MinScore;`
    <img width="212" alt="p7" src="https://user-images.githubusercontent.com/113796019/206625892-44955cca-3558-4753-b4a2-45916ed08e62.png">

8.  What is the average GPA required for a university? 

        Create View UniAvgGPA As Select university_name, avg(CGPA) from  University left join Requirements on University.university_id = Requirements.university_id;

    `Select * from UniAvgGPA;`
    <img width="154" alt="p8" src="https://user-images.githubusercontent.com/113796019/206625938-08371b3b-77f5-4327-8db7-d810b7ac25bb.png">

9.  Are there any scholarships available for international students ? 

    Scholarship details are not included in the database.

10. What are the chances of getting an admit in the university based of the students profile? 

        Create View UniCGA As Select University_name, chance_of_admit from University left join Requirements on University.university_id = Requirements.university_id where GRE = 320 AND TOEFL = 104 AND university_name = 'Northeastern University';

    `Select * from UniCGA;`
    <img width="205" alt="p10" src="https://user-images.githubusercontent.com/113796019/206625968-8976362a-d231-4f0f-b31b-24e17ab4d497.png">
      
## Somesh:

1.  Search for universities which ranks between top 20-30.

        Create View UniRankBetween As Select University_name, national_rank from University where national_rank BETWEEN 20 and 30;

    `Select * from UniRankBetween;`
    <img width="282" alt="somesh1" src="https://user-images.githubusercontent.com/113796019/206626112-7d7c95d3-cf90-4fb0-ad2b-2823eeec916a.png">

2.  View the universities which has CGPA cutoff of 3.5 and above.

        Create View UniCGPACutoff As Select University.University_Id, university_name from University left join Requirements on  University.university_id = Requirements.university_id where CGPA >= 3.5;

     `Select * from UniCGPACutoff;`
     <img width="270" alt="somesh2" src="https://user-images.githubusercontent.com/113796019/206626141-1ffc77ff-cb29-4caf-9638-711c5a443ca0.png">

3.  Which universities require a minimum score of 7 bands in IELTS and TOEFL > = 100?

    The dataset does not have details of IELTS.

        Create View UniMinTOEFL As Select University.University_Id, University_Name, GRE, TOEFL from University left join Requirements On University.University_Id = Requirements.University_Id where TOEFL >= 100;

    `Select * from UniMinTOEFL;`
    <img width="343" alt="somesh3" src="https://user-images.githubusercontent.com/113796019/206626185-3cd32a15-4ef9-412b-8933-1daba52c2c1b.png">

4.  What is the acceptance rate of students with a CGPA > = 7?

        Create View AccRateWithCGPA As Select University.University_Id, university_name, Chance_of_Admit from University left join requirements on University.University_ID = Requirements.University_ID where CGPA >= 7;

    `Select * from AccRateWithCGPA;`
    <img width="340" alt="somesh4" src="https://user-images.githubusercontent.com/113796019/206626227-dfd20af0-20b4-4425-bf86-08f9504c06af.png">

5.  View the universities which offer course of “Computer science and engineering”.

    The dataset does not have details of courses.

6.  View the course which has requirements of IELTS<7.0 band.

    The dataset does not have details of courses.

7.  View the twitter username for the tweets related to Princeton University.

    The dataset does not have a details of twitter scap data.

8.  Which universities have a higher acceptance rate and a lower graduation rate?

    The dataset does not have details of graduation rate.

9.  Which universities have a high intake of international students in fall 2022?

    The dataset does not have details of intake of international students.

10. Determine which university is in a developed location and has a vast job market (city or rural).

    No such information present in the dataset.

11. How many universities have a high graduation rate in 2021?

    The dataset does not have details of graduation rate.

12. Which universities have IVY league status and view acceptance rate?

    The dataset does not have details of IVY league status.
 
13. Determine which universities have GRE requirements such as Verbal > = 155, Quants > = 160, and AWA > = 3.

    All the universities in the dataset have combined GRE score requirement.
    
14. What is the most popular course of study in the top 10–20 universities?

    The dataset does not have a details of courses.

15. Which of the following private universities doesn’t have GRE or English proficiency exam requirements for application?

    All the universities in the dataset have combined GRE and IELTS/TOEFL requirement.

