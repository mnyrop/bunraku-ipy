import pandas as pd

authors_df = pd.read_csv('authors.csv')
play_auth_df = pd.read_csv('authors_plays.csv')

authors_w_play_id = pd.merge(authors_df, play_auth_df, on='author_id', how='inner')

auth_id_list = list(authors_w_play_id.author_id.unique())
cols =  authors_w_play_id.columns
final_auth_df = pd.DataFrame({})

for id_num in auth_id_list:
    temp_auth = authors_w_play_id.loc[authors_w_play_id['author_id'] == id_num]

    vals = []
    for col in cols:
        vals.append(temp_auth[:1][col].values[0])

    temp_dict = dict(zip(cols, vals))
    temp_auth_plays = list(temp_auth['play_id'])
    temp_dict['play_id'] = temp_auth_plays

    final_auth_df = final_auth_df.append(temp_dict, ignore_index=True)

final_auth_df['author_id'] = final_auth_df['author_id'].astype(int).astype('str')

final_auth_df.to_json('authors_with_play_id_array.json', orient="records", force_ascii=False)
