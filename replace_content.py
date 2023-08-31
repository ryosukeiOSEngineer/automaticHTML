# 置換処理実施
def link_generator(ec_site, xxx):
    functions = {
        'amazon': amazon_search,
        'rakuten': rakuten_search,
        'google': google_search,
        'cinii': cinii_search,
        'jstage': jstage_search,
        'IRDB': IRDB_search,
    }
    
    if ec_site not in functions:
        raise ValueError(f"{ec_site} は、なにかしらの理由で表示できません。")

    return functions[ec_site](xxx)


def replace_placeholders(html_template, df):
    def replace_merit_list(merits):
        return '\n'.join([f'<li>{merit}</li>' for merit in merits])
    
    placeholders_mapping = {
        # １-赤
        '<p>XXXは「安い」「綺麗になる」「健康的になる」などが魅力です。</p>': (get_merits1, {}),
        
        # １-青
        '<p>意味があるとされるおすすめポイントは「美肌になれる」「飲みやすい」「誰でも飲める」などがあります。</p>': (get_merits2, {}),
        

        # １-緑
        '<ul class="is-style-check_list has-swl-pale-02-background-color has-background">\n<li>活性酵素を除去してくれる</li>\n<li>変な味はしないので一般的な飲料として飲める</li>\n<li>アンチエイジング効果がある</li>\n<li>ダイエット効果がある</li>\n<li>美肌効果がある</li>\n<li>便秘が解消される</li>\n</ul>': (get_merits3, {}),
        
        # ２-赤
        '<ul class="is-style-check_list">': (merit_lst, {'post_process': replace_merit_list}),
        
        # ３-赤 タブ
        '<button role="tab" class="c-tabList__button" aria-selected="true" aria-controls="tab-6deac381-0" data-onclick="tabControl">体内の活性化</button>': (get_one_word_description, {'wrapper': '<button role="tab" class="c-tabList__button" aria-selected="true" aria-controls="tab-6deac381-0" data-onclick="tabControl">{}</button>'}),
        
        # ４-青
        '<ul class="is-style-triangle_list">\n<li>価格が高い</li>\n</ul>': (replace_demerit_list, {}),
        
        # ４-赤
        '<p>意味ない理由として「怪しい」「個人差がありすぎる」「理解するまで時間がかかる」などのコメントがありました。</p>':(get_demerits, {}),
        
        # ６-赤
        '<ul class="is-style-good_list">\n<li><a href="#kouka-1" automate_uuid="d3495264-e1e1-4675-84cb-c872e762cc7d" data-nodal="">簡単に綺麗を保てる</a></li>\n<li><a href="#kouka-2" automate_uuid="3087e4ad-8612-461b-a0fc-6ff92220ce85" data-nodal="">家族みんなで楽しめる</a></li>\n<li><a href="#kouka-3" automate_uuid="9740b60d-80c7-4676-8755-257f3bae9e4a" data-nodal="">飲むだけでアンチエイジングできる</a></li>\n<li><a href="#kouka-4" automate_uuid="a246317f-35a5-40a4-95fe-3819e40e41f0" data-nodal="">ダイエットにオススメ</a></li>\n</ul>': (get_experiences_lst, {}),
        
        # ６-青 h3
        '<h3 class="wp-block-heading" id="kouka-1">簡単に綺麗を保てる</h3>': (replace_experiences, {'index': 0, 'type': 'h3'}),
        '<p>色々な商品を試しましたが…</p>': (replace_experiences, {'index': 0, 'type': 'p'}),
        '<img decoding="async" loading="lazy" src="https://iminain.com/wp-content/uploads/2023/06/icon-6-150x150.png" alt="" class="c-balloon__iconImg" width="80px" height="80px">': (replace_experiences, {'index': 0, 'type': 'img'}),
        
        # ７-赤
        '<p>特に「便秘気味な人」「手軽に美を手に入れたい人」「安さを求める人」におすすめです。</p>':(get_recommends, {}),

        # ７-青
        '<ul class="is-style-check_list">\n<li>家族みんなで健康に取り組みたい人</li>\n<li>アンチエイジングに興味のある人</li>\n<li>健康志向の人</li>\n<li>健康に値段がかけられる人</li>\n<li>アンチエイジング効果を求めている人</li>\n<li>お水に値段がかけられる人</li>\n<li>ダイエットしたい人</li>\n<li>健康に気を使っている人</li>\n<li>便秘の人</li>\n</ul>':(recommends_lst, {}),

        # ８-赤
        '<p>XXXは安い、綺麗になる、健康的になるのが魅力です。【意味ナイン】では、XXXは意味ないのか、意味あるのか調査し、評判やコメント、おすすめ代替案について紹介しています。</p>':(get_merits2, {}),

        # Amazon検索
        'amazon_placeholder': (amazon_search, {'search_term': "xxx"}),

        # 楽天
        'rakuten_placeholder': (rakuten_search, {'search_term': "xxx"}),

        # yahoo
        'yahoo_placeholder': (yahoo_search, {'search_term': "xxx"}),

        # google
        'google_placeholder': (google_search, {'search_term': "xxx"}),

        # cinii
        'cinii_placeholder': (cinii_search, {'search_term': "xxx"}),

        # jstage
        'jstage_placeholder': (jstage_search, {'search_term': "xxx"}),

        # IRDB
        'IRDB_placeholder': (IRDB_search, {'search_term': "xxx"}),

}

    }
    
    for placeholder, (func, args) in placeholders_mapping.items():
        # 関数の存在の確認
        if not callable(func):
            raise ValueError(f"Function {func} is not callable or not defined.")

        # プレースホルダの存在の確認
        if placeholder not in html_template:
            raise ValueError(f"Placeholder {placeholder} not found in the template.")

        # 関数の実行中のエラー
        try:
            html_content = func(df, **args)
            # ここで置換処理を行う
            html_template = html_template.replace(placeholder, html_content)
        except Exception as e:
            raise RuntimeError(f"Error executing function {func}: {str(e)}")

        # 'args'の適切なキーの確認
        if 'post_process' in args and not callable(args['post_process']):
            raise ValueError(f"'post_process' in args is not callable.")
            

    return html_template



