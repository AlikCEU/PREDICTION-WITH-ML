# README: Study on Tolerance

## Dataset Description

- **Name**: World Values Survey (WVS) - Subset
- **Source**: World Values Survey Wave 7 (2017-2022)
- **Description**: This dataset contains responses from a global survey covering social, economic, and political values. The data provides insights into individuals' attitudes toward diversity, trust in institutions, and perceptions of different social groups.

## File Location

- **Dataset Path**: `/mnt/data/WVS_subset.csv`
- **Codebook Path**: `/mnt/data/WVS_codebook.pdf`

## Research Question

**How do trust levels and social attitudes influence people's tolerance toward various social groups?**

## Selected Variables (17 Variables)

### Tolerance and Social Attitudes:

1. **Q19** – Unwillingness to have people of a different race as neighbors
2. **Q21** – Unwillingness to have immigrants as neighbors
3. **Q22** – Unwillingness to have homosexuals as neighbors
4. **Q23** – Unwillingness to have people of a different religion as neighbors
5. **Q26** – Unwillingness to have people speaking a different language as neighbors
6. **Q36** – Homosexual couples are as good parents as heterosexual couples
7. **Q62** – Trust in people of a different religion
8. **Q63** – Trust in people of a different nationality

### Gender Attitudes:

9. **Q29** – Men make better politicians than women
10. **Q31** – Men make better business leaders than women
11. **Q33** – When jobs are scarce, men should have more right to a job than women
12. **Q35** – If a woman earns more than her husband, it causes problems
13. **Q80** – Trust in women's movements

### Relationship Between Tolerance and Social/Economic Factors:

14. **Q46** – Level of happiness
15. **Q49** – Life satisfaction
16. **Q57** – General trust in people
17. **Q71** – Trust in government

## Descriptive Statistics for Key Variables

The following five variables have been selected as the most important, representing different aspects of tolerance, trust, and societal well-being:

| Variable                          | Description                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Q19 (Race Tolerance)**          | Measures unwillingness to have people of a different race as neighbors. A lower score indicates greater racial tolerance. |
| **Q22 (LGBT Tolerance)**          | Captures attitudes toward LGBTQ+ individuals, specifically whether respondents would accept homosexuals as neighbors. |
| **Q71 (Trust in Government)**     | Measures confidence in government institutions and their ability to function effectively. Higher trust levels may correlate with greater societal stability and acceptance of diversity. |
| **Q49 (Life Satisfaction)**       | Measures overall life satisfaction on a scale from 1 to 10. Higher scores indicate greater happiness and personal well-being. |
| **Q57 (General Trust in People)** | Assesses whether respondents believe that most people can be trusted or that one should be cautious in interactions. |

## Detailed Descriptive Statistics (Excluding Missing Values)

| Variable                      | Count  | Mean | Std Dev | Min | 25% | 50% (Median) | 75% | Max |
| ----------------------------- | ------ | ---- | ------- | --- | --- | ------------ | --- | --- |
| Q19 (Race Tolerance)          | 91,454 | 2.13 | 0.76    | 1   | 2   | 2            | 2   | 3   |
| Q22 (LGBT Tolerance)          | 91,454 | 1.76 | 0.98    | 1   | 1   | 2            | 2   | 3   |
| Q71 (Trust in Government)     | 91,454 | 2.56 | 1.20    | 1   | 2   | 3            | 3   | 5   |
| Q49 (Life Satisfaction)       | 91,454 | 6.85 | 2.11    | 1   | 5   | 7            | 8   | 10  |
| Q57 (General Trust in People) | 91,454 | 1.95 | 0.85    | 1   | 1   | 2            | 2   | 3   |

## Handling Missing Values

- **Identified Missing Values**: `-5`, `-4`, `-2` were excluded from computations.
- **Impact on Analysis**: With missing values excluded, statistical calculations more accurately reflect valid responses.

## Key Takeaways from Analysis

- **Trust and Tolerance Correlation**: Higher levels of general trust in people and trust in government seem to correlate with greater tolerance toward different racial and social groups.
- **Happiness and Acceptance**: Individuals with higher life satisfaction scores tend to have more tolerant attitudes towards diversity.
- **LGBT and Race Tolerance**: The distribution of responses indicates that while a significant portion of respondents show tolerance, there is still notable resistance towards LGBT and racial diversity in some demographics.
- **Cultural and Political Influence**: Differences in trust in government might be reflective of broader socio-political contexts, where individuals in stable governance systems exhibit more openness towards others.
- **Policy Implications**: Efforts to increase trust in social institutions and enhance general happiness may contribute to fostering more inclusive and tolerant societies.

## Usage Notes

- **Variable Scaling**: Most variables are ordinal, so appropriate statistical tests (e.g., Spearman correlation, logistic regression) should be used.
- **Cultural Differences**: Responses vary by country and culture. Interpret findings considering regional differences in social norms.
- **Data Cleaning**: Ensure missing values are accounted for in any future modeling or visualization efforts.

---

**Author:** Allakhverdi Agakishiev  
**Date:** 02.03.2025
**Course:** Data Analysis with AI - Week 01

