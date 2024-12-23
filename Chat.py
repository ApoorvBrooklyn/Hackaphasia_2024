import requests
from bs4 import BeautifulSoup
import openai
import json



# Sample JSON Data (Assumed preloaded)
data = {
    "schemes": [
      {
        "name": "Beti Bachao Beti Padhao",
        "category": "Girl Child Support",
        "benefits": "Awareness and improvement in the welfare of the girl child, funds for education, and survival",
        "eligibility": "Open to families with a girl child; focus on districts with low Child Sex Ratio"
      },
      {
        "name": "Sukanya Samriddhi Yojana",
        "category": "Girl Child Financial Support",
        "benefits": "High-interest savings account for girl child's education and marriage expenses",
        "eligibility": "Girls below 10 years; family income restrictions for tax benefits under Section 80C"
      },
      {
        "name": "Scheduled Caste Post-Matric Scholarship",
        "category": "Education Scholarship",
        "benefits": "Tuition fee reimbursement and living allowances",
        "eligibility": "SC students pursuing post-matric education; family income below ₹2.5 lakh annually"
      },
      {
        "name": "Saksham Scholarship",
        "category": "Disability Support",
        "benefits": "₹50,000 annual scholarship for differently-abled students",
        "eligibility": "Differently-abled students with family income below ₹8 lakh annually; enrolled in technical courses"
      },
      {
        "name": "Integrated Child Development Services (ICDS)",
        "category": "Child Welfare",
        "benefits": "Health, nutrition, preschool education, and vaccination for children and pregnant women",
        "eligibility": "Open to children under 6 years, pregnant/lactating women in rural or urban slum areas"
      },
      {
        "name": "National Means-cum-Merit Scholarship (NMMSS)",
        "category": "Education Scholarship",
        "benefits": "₹12,000 per annum for students in Class IX to XII",
        "eligibility": "Students scoring at least 55% in Class VIII; family income below ₹1.5 lakh annually"
      },
      {
        "name": "Prime Minister's Special Scholarship Scheme(PMSSS)",
        "category": "Education Support",
        "benefits": "Financial aid for higher education in professional courses",
        "eligibility": "Students from J&K pursuing higher education outside the state"
      },
      {
        "name": "Midday Meal Programs",
        "category": "Child Nutrition",
        "benefits": "Free cooked meals to improve enrollment and reduce hunger",
        "eligibility": "Students in government and government-aided primary schools"
      },
      {
        "name": "Kasturba Gandhi Balika Vidyalaya",
        "category": "Girl Child Education",
        "benefits": "Residential schooling for girls from disadvantaged groups",
        "eligibility": "Girls from SC/ST/OBC/minority communities in educationally backward blocks"
      },
      {
        "name": "Balika Samriddhi Yojana",
        "category": "Girl Child Support",
        "benefits": "Cash incentives for girl child's education",
        "eligibility": "Girls born in families below the poverty line"
      },
      {
        "name": "Samagra Shiksha",
        "category": "Education Support",
        "benefits": "Financial support for school education and teacher training",
        "eligibility": "All students from government schools, especially from disadvantaged groups"
      },
      {
        "name": "Mukhyamantri Rajshri Yojana",
        "category": "Girl Child Support",
        "benefits": "Financial incentives for girls at birth, enrollment in school, and higher education",
        "eligibility": "Girls born in Rajasthan to families with income below a certain threshold"
      },
      {
        "name": "Pradhan Mantri Kaushal Vikas Yojana (PMKVY)",
        "category": "Skill Development",
        "benefits": "Free skill training and certification for employment",
        "eligibility": "Youth aged 18–35 years; priority for underprivileged and unemployed individuals"
      },
      {
        "name": "Scheme of Apprenticeship Training",
        "category": "Skill Development",
        "benefits": "Stipend and practical training opportunities",
        "eligibility": "Students pursuing higher education or vocational courses"
      },
      {
        "name": "Sarva Shiksha Abhiyan",
        "category": "Education Support",
        "benefits": "Universal access to free elementary education",
        "eligibility": "All children aged 6–14 years"
      },
      {
        "name": "Rashtriya Madhyamik Shiksha Abhiyan (RMSA)",
        "category": "Education Support",
        "benefits": "Improvement in secondary education infrastructure and access",
        "eligibility": "Students in government and government-aided secondary schools"
      },
      {
        "name": "Free and Compulsory Education",
        "category": "Education Rights",
        "benefits": "Right to free education under RTE Act",
        "eligibility": "All children aged 6–14 years in India"
      },
      {
        "name": "CBSE Udaan Scheme",
        "category": "Girl Child Education",
        "benefits": "Free study material and resources for girls in engineering aspirants",
        "eligibility": "Girls enrolled in Class XI and XII; family income below ₹6 lakh annually"
      },
      {
        "name": "Nanda Devi Kanya Yojana",
        "category": "Girl Child Support",
        "benefits": "Financial support for the education and welfare of girl children",
        "eligibility": "Girls born in Uttarakhand to families below the poverty line"
      },
      {
        "name": "Pre-Matric Scholarship to SC Students",
        "category": "Education Scholarship",
        "benefits": "Financial assistance for SC students in Classes IX and X",
        "eligibility": "SC students with family income below ₹2 lakh annually"
      },
      {
        "name": "Integrated Child Protection Scheme (ICPS)",
        "category": "Child Welfare",
        "benefits": "Aims to improve the well-being of children in difficult circumstances and reduce vulnerabilities",
        "eligibility": "Children in vulnerable and difficult circumstances"
      },
      {
        "name": "Rajiv Gandhi Scheme for Empowerment of Adolescent Girls (SABLA)",
        "category": "Girl Child Empowerment",
        "benefits": "Focuses on the all-round development of adolescent girls aged 11-18 years through education and vocational training",
        "eligibility": "Adolescent girls aged 11-18 years, especially from disadvantaged backgrounds"
      },
      {
        "name": "Indira Gandhi Matritva Sahyog Yojana (IGMSY)",
        "category": "Maternal Support",
        "benefits": "A conditional cash transfer scheme for pregnant and lactating women to improve health and nutrition",
        "eligibility": "Pregnant and lactating women meeting specific health and income criteria"
      },
      {
        "name": "National Child Labour Project (NCLP)",
        "category": "Child Protection",
        "benefits": "Aims to withdraw children from hazardous occupations and mainstream them into formal education",
        "eligibility": "Children engaged in hazardous labor, aged 9-14 years"
      },
      {
        "name": "Mid-Day Meal Scheme",
        "category": "Child Nutrition",
        "benefits": "Provides nutritious meals to school children to enhance enrollment and retention in schools",
        "eligibility": "Students in government and government-aided schools"
      },
      {
        "name": "National Scheme for Incentives to Girls for Secondary Education (NSIGSE)",
        "category": "Girl Child Education",
        "benefits": "Encourages girls from SC/ST communities to pursue secondary education with financial incentives",
        "eligibility": "Girls from SC/ST communities enrolled in secondary education"
      },
      {
        "name": "Ladli Lakshmi Yojana",
        "category": "Girl Child Support",
        "benefits": "Provides financial support for the education of girls from economically weaker backgrounds in Madhya Pradesh",
        "eligibility": "Girls born in Madhya Pradesh to families meeting economic criteria"
      },
      {
        "name": "Majhi Kanya Bhagyashree Scheme",
        "category": "Girl Child Support",
        "benefits": "Offers financial assistance for the education of girls in Maharashtra",
        "eligibility": "Families with girl children in Maharashtra, especially economically weaker sections"
      },
      {
        "name": "Gharaunda (Group Home for Adults)",
        "category": "Disability Support",
        "benefits": "Aims at providing care for adults with disabilities, indirectly supporting their educational needs through vocational training",
        "eligibility": "Adults with disabilities requiring residential care and skill development"
      },
      {
        "name": "Gyan Prabha",
        "category": "Disability Support",
        "benefits": "Provides educational support for persons with disabilities pursuing vocational courses leading to employment",
        "eligibility": "Persons with disabilities pursuing vocational training"
      },
      {
        "name": "PM CARES for Children",
        "category": "Child Support",
        "benefits": "Financial support and educational assistance for children who lost parents due to COVID-19",
        "eligibility": "Children orphaned due to COVID-19"
      },
      {
        "name": "DISHA (Early Intervention and School Readiness Scheme)",
        "category": "Disability Support",
        "benefits": "Supports early intervention for children with disabilities aged 0-10 years",
        "eligibility": "Children with disabilities aged 0-10 years"
      },
      {
        "name": "VIKAAS (Day Care)",
        "category": "Disability Support",
        "benefits": "Daycare facilities aimed at enhancing skills of persons with disabilities transitioning into adulthood",
        "eligibility": "Persons with disabilities requiring daycare facilities"
      },
      {
        "name": "SAMARTH (Respite Care)",
        "category": "Disability Support",
        "benefits": "Provides respite care services for orphans and persons with disabilities from low-income families",
        "eligibility": "Orphans and persons with disabilities from low-income families"
      },
      {
        "name": "Prerna (Marketing Assistance)",
        "category": "Disability Empowerment",
        "benefits": "Supports marketing products made by persons with disabilities, fostering skill development and empowerment through entrepreneurship",
        "eligibility": "Persons with disabilities engaged in entrepreneurial activities"
      }
    ],
    "categories": [
      "Girl Child Support",
      "Education Scholarship",
      "Disability Support",
      "Child Welfare",
      "Education Support",
      "Child Nutrition",
      "Girl Child Education",
      "Skill Development",
      "Girl Child Empowerment",
      "Child Support",
      "Education Rights",
      "Maternal Support",
      "Child Protection",
      "Disability Empowerment"
    ],
    "metadata": {
      "total_schemes": 44,
      "last_updated": "2024-12-05"
    }
  }

def find_scheme_by_category(category):
    return [scheme for scheme in data['schemes'] if scheme['category'].lower() == category.lower()]

def find_scheme_by_name(name):
    return next((scheme for scheme in data['schemes'] if scheme['name'].lower() == name.lower()), None)

def search_web(query):
    """Search the web for fallback results."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(google_search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        snippets = [result.get_text() for result in search_results[:5]]  # Limit to top 5 results
        return snippets
    else:
        return ["Unable to fetch search results."]

def generate_ai_response(prompt):
    
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error with AI response generation: {e}"

def chatbot_response(prompt):
    # Match intent with JSON data
    if "schemes for" in prompt.lower():
        category = prompt.split("schemes for")[1].strip()
        schemes = find_scheme_by_category(category)
        if schemes:
            return "\n".join([scheme['name'] for scheme in schemes])
    elif "tell me about" in prompt.lower():
        scheme_name = prompt.split("tell me about")[1].strip()
        scheme = find_scheme_by_name(scheme_name)
        if scheme:
            return (f"Scheme Name: {scheme['name']}\n"
                    f"Benefits: {scheme['benefits']}\n"
                    f"Eligibility: {scheme['eligibility']}")

    # Web fallback
    search_results = search_web(prompt)
    if search_results:
        return "\n".join(search_results)

    # AI fallback
    return generate_ai_response(prompt)

def start_chatbot(user_input):
    response = chatbot_response(user_input)
    return response

    

# Example usage
if __name__ == "__main__":
    start_chatbot()
