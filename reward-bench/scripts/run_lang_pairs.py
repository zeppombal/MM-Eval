import argparse

import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scores_path', type=str,
                        help='Path to the scores .json file file')
    parser.add_argument('--en_subset_name', type=str, default=None, required=False,
                        help='Name of the English subset (xstorycloze_en, belebele_eng_Latn, etc.)')
    args = parser.parse_args()

    en_subset_name = args.en_subset_name

    if en_subset_name is None:
        if 'xstorycloze' in args.scores_path:
            en_subset_name = 'xstorycloze_en'
        elif 'belebele' in args.scores_path:
            en_subset_name = 'belebele_eng_Latn'
        else:
            raise ValueError(
                'Please provide the name of the English subset')

    df = pd.read_json(args.scores_path)
    df['scores_chosen'] = df['scores_chosen'].apply(lambda x: float(x[0]))
    df['scores_rejected'] = df['scores_rejected'].apply(lambda x: float(x[0]))

    subset_dfs = {k: v for k, v in df.groupby('subset')}
    en_df = subset_dfs.pop(en_subset_name)

    total_scores = {}

    for i, subset_df in enumerate(subset_dfs.values()):
        lang = subset_df.iloc[0]['subset'].split('_')[-1]
        tmp_df = pd.DataFrame(data={'en_scores_chosen': en_df['scores_chosen'].to_list(), 'en_scores_rejected': en_df['scores_rejected'].to_list(
        ), 'target_scores_chosen': subset_df['scores_chosen'].to_list(), 'target_scores_rejected': subset_df['scores_rejected'].to_list()})
        tmp_df['en_chosen_wins'] = (
            tmp_df['en_scores_chosen'] > tmp_df['target_scores_chosen']).astype(int)
        tmp_df['en_rejected_wins'] = (
            tmp_df['en_scores_rejected'] > tmp_df['target_scores_rejected']).astype(int)

        en_chosen_win_rate = sum(tmp_df['en_chosen_wins']) / len(tmp_df)
        en_rejected_win_rate = sum(tmp_df['en_rejected_wins']) / len(tmp_df)

        total_scores[lang] = {'en_chosen_win_rate': en_chosen_win_rate,
                              'en_rejected_win_rate': en_rejected_win_rate}

    lang_pairs_scores = pd.DataFrame.from_dict(total_scores, orient='index')
    lang_pairs_scores.to_json(
        args.scores_path.replace('.json', f'_lang_pairs.json'))
    print(lang_pairs_scores)
