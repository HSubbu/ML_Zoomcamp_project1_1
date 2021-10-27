#Check if model can predict with given data
import pickle

#loading the model and check
with open("project_one_model.pkl","rb") as f_in:
    dv,model_loaded = pickle.load(f_in)

candidate = [{'gender': 'M',
  'ssc_p': 71.0,
  'ssc_b': 'Central',
  'hsc_p': 58.66,
  'hsc_b': 'Central',
  'hsc_s': 'Science',
  'degree_p': 58.0,
  'degree_t': 'Sci&Tech',
  'etest_p': 56.0,
  'mba_p': 61.3,
  'specialisation': 'Mkt&Fin',
  'workex': 'Yes',
  }]
candidate_encoded = dv.transform(candidate)
print(f'Probability of candidate getting placement {model_loaded.predict_proba(candidate_encoded)[:,1]}')