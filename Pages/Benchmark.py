"""
@who:
@where: 
@when: 
@what: 
"""

import streamlit as st


from Utils.utils import *
from Utils.constants import *

# Use session state to store CURRENT_WINDOW_BENCHMARK to persist across user interactions
if 'CURRENT_WINDOW_BENCHMARK' not in st.session_state:
    st.session_state.CURRENT_WINDOW_BENCHMARK = 0

st.markdown(text_tab_benchmark)

tab_playground, tab_benchmark = st.tabs(
        ["Metrics Comparaison", "Visual Comparaison"]
    )
    
with tab_playground:
    run_metric_comparaison_frame()

with tab_benchmark:
    col1_1, col1_2, col1_3 = st.columns(3)

    with col1_1:
        ts_name = st.selectbox(
            "Choose a load curve", list_name_ts, index=0
        )
    with col1_2:
        length = st.selectbox(
            "Choose the window length:", lengths_list, index=2
        )
    with col1_3:
        appliance_selected = st.selectbox(
            "Choose devices:", devices_list_ideal if 'IDEAL' in ts_name else devices_list_refit_ukdale,
        )

    models = ['ResNetEnsemble']


    colcontrol_1, colcontrol_2, colcontrol_3 = st.columns([0.2, 0.8, 0.2])
    with colcontrol_1:
        if st.button(":rewind: **Prev.**", type="primary"):
            st.session_state.CURRENT_WINDOW_BENCHMARK -= 1
    with colcontrol_3:
        if st.button("**Next** :fast_forward:", type="primary"):
            st.session_state.CURRENT_WINDOW_BENCHMARK += 1

    # Load the time series data
    df, window_size = get_time_series_data(ts_name, length=length)
    n_win = len(df) // window_size

    # Ensure CURRENT_WINDOW_BENCHMARK stays within valid bounds
    if st.session_state.CURRENT_WINDOW_BENCHMARK >= n_win:
        st.session_state.CURRENT_WINDOW_BENCHMARK = 0
    elif st.session_state.CURRENT_WINDOW_BENCHMARK < 0:
        st.session_state.CURRENT_WINDOW_BENCHMARK = n_win - 1


    # Display window range
    with colcontrol_2:
        st.markdown("<p style='text-align: center;'> <b>from</b> <i>{}</i> <b>to</b> <i>{}</i> </p>".format(
            df.iloc[st.session_state.CURRENT_WINDOW_BENCHMARK * window_size: (st.session_state.CURRENT_WINDOW_BENCHMARK + 1) * window_size].index[0],
            df.iloc[st.session_state.CURRENT_WINDOW_BENCHMARK * window_size: (st.session_state.CURRENT_WINDOW_BENCHMARK + 1) * window_size].index[-1]),
            unsafe_allow_html=True)
        
        pred_status_flag = st.toggle('Predict Status')

        dataset_name = 'IDEAL'
        pred = pd.read_csv(os.getcwd()+'/Pred/IDEAL/Dishwasher/IDEAL_House175_2018-01.gzip', parse_dates=['Time'], index_col=['Time'], compression='gzip')
        
        pred_nilmcam    = pred_one_window_nilmcam(st.session_state.CURRENT_WINDOW_BENCHMARK, pred, window_size, dataset_name, [appliance_selected])
        fig_comparaison = plot_one_window_benchmark(st.session_state.CURRENT_WINDOW_BENCHMARK, pred, window_size, 'Dishwasher', pred_nilmcam)
        st.plotly_chart(fig_comparaison, use_container_width=True)
