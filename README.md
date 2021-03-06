**Title:** 

Effect of political partisanship on racial bias in police stops

**Abstract:**

Pierson et al. have previously collected a dataset about traffic stops accross the USA. Their dataset suggests that there is a racial bias in police stops decisions. However they did not investigate the source of this racial bias. We therefore propose an extension to their work by inspecting potential disparities between the states based on their political dominance. 
An Oxford study supports the fact that an "individual's personality significantly contributes to contemporary political allegiance and engagement" [1]. Thus we hypothesize that the political dominance of a state reflects the average personality of it's population, and therefore their decision-making, which could be observed through differences in racial bias in police stops. In other words, this study aims to see whether the state political affiliation impacts the racial bias in police stops.

[1] https://www.politicalpersonality.org/election/the-personality-of-politics-how-personality-impacts-political-engagement-affiliation/

**Research questions:**
    
    1. Is there a correlation between political partisanship and racial bias across states? 
    2. How do search rates behave in time across political partisanship?

**Proposed datasets:**

    - Partisanship datas, rebuilt by our team, available here: https://www.ncsl.org/research/about-state-legislatures/partisan-composition.aspx
    - State Patrol stops datas available here: https://openpolicing.stanford.edu/data/

**Methods:**

    - Data acquisition: we will manually convert (from pdf to csv) a yearly partisanship dataset, for all states.
    - Data collection: to merge the state patrol stops dataset and the political partisanship dataset, we need to manually modify IDs (e.g state names).
    - Create search rates: we will create search rates by applying per year a logistic regression on the datas to get the probabilty of beeing searched when stopped.
    - Edit: In the end we gave up on the logistic regression as it would strongly bias our analysis afterwards. Instead, we used the empirical means to build the search rates.
    - Comparing racial bias across states: we will implement a linear regression for each race, state and time period analyze trends in search decisions.
    - Edit: we used bootstrapping to build confidence intervals, as well as linear regression in the time-wise analysis. 

**Proposed timeline:**

Week 1: 

    - downloading datasets
    - manually create state political partisanship dataset
    - merging all datasets
    - beginning of analysis
    - get used to jekyll
    
Week 2: 

    - implementation of logistic regression to get rates (to be defined) per year
    - implementation of linear regression to compare races and states (per time period)
    - continuation of analysis

Week 3: 

    - data story
    - report
    - pitch
    - individual figure 3a replication
    - 18th december: rdv to our graveyard for the pitch

**Organization within the team:**

During the First week, Axel will download all datasets, manually create the partisanship dataset and select the states to consider in the analysis. 
Antoine and Nino will start analyzing the dataset and get used to Jekyll

During the second week, Axel will perform a logistic regression to set search rates per year. Antoine and Nino will use this logistic regression to generate the first interactive figures and implement the linear regression.

During the third week, Antoine and Nino will continue their analysis and include figures in the data story. All together we will record a nice pitch.

Edit: We found out that logistic regression would strongly bias our search rates, thus we changed the analysis using empirical search rates.

**Questions for TAs**

- Is it relevant to use a logistic regression to get search rates (predictions)? 
- Are our questions specific enough? 
- Does it matter if we do not compare all of the states (as datas are not available for every years in every states...)? 
