import random

SENIORITY = (
    'Associate',
    'Black Belt',
    'Chief',
    'Full Stack',
    'Head',
    'Heavyweight',
    'Junior',
    'Lead',
    'Middleweight',
    'Principal',
    'Senior'
)
PRACTICE = (
    'Augmented Reality',
    'Content',
    'Design',
    'Embodied Interactions',
    'Front End',
    'Gaming',
    'GUI',
    'Human Factors',
    'IxD',
    'Information',
    'Intelligent Systems',
    'Interaction',
    'Machine Learning',
    'UI/UX',
    'Usability',
    'User Centered Design',
    'User Experience',
    'User Interface',
    'Virtual Reality',
    'Visual'
)
ROLE = (
    'Alchemist',
    'Analyst',
    'Architect',
    'Champion',
    'Consultant',
    'Crusader',
    'Designer',
    'Developer',
    'Director',
    'Evangelist',
    'Expert',
    'Extraordinaire',
    'Fusionist',
    'Generalist',
    'God',
    'Guru',
    'Hero',
    'Interventionist',
    'Magician',
    'Manager',
    'Ninja',
    'Officer',
    'Producer',
    'Practitioner',
    'Professional',
    'Prophet',
    'Researcher',
    'Rock Star',
    'Sorcerer',
    'Specialist',
    'Strategist',
    'Technologist',
    'Unicorn'
)

def uxgenerator():
    return random.choice(SENIORITY), random.choice(PRACTICE), random.choice(ROLE)

def main():
    return uxgenerator()

if __name__ == "__main__":
    print main()