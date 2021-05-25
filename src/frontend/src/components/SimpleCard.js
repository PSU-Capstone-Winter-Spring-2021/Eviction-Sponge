import React from 'react';
// import { makeStyles } from 'material-ui/core/styles';
import Card from '@material-ui/core/Card';
// import CardActions from 'material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
// import Button from 'material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import 'react-bootstrap';
import { Link } from "react-router-dom";
import axios from 'axios';
import { ThemeConsumer } from 'react-bootstrap/esm/ThemeProvider';

export default class SimpleCard extends React.Component{
    constructor(props) {
                super(props);
                this.state = {
                    caseNum: Object.keys(this.props.res),
                    result: this.props.res,
                    casePage: {}
                  };
    }

    async componentDidMount() {
        console.log("calling to: " + `/case-detail/${this.state.result[this.state.caseNum].case_id}`)
        await axios.get(`/case-detail/${parseInt(this.state.result[this.state.caseNum].case_id)}`).then(res => {
            if (res) {
                this.setState({casePage: res.data})
                console.log(res.data)
            }
        })
    }

    handleClick(e) {
        e.preventDefault()
        let oeciPage = window.open()
        oeciPage.document.open()
        oeciPage.document.write(this.state.casePage)
        oeciPage.document.close()

    }

    render (){
    const {caseNum} = this.state;
    const {location: county_name, style: case_name , status, eligibility, closed_dagit te: date_of_judgement, case_id} = this.state.result[caseNum];
    console.log("Id is; " + case_id)
    return(
    <div className = "bg-light">
        <Card className='bg-light border'>
        <CardContent>
            <Typography className={caseNum} color="textSecondary" gutterBottom>
                <a href= "#" onClick={this.handleClick.bind(this)} target="blank">
                    {caseNum} 
                </a>
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            Location: {county_name}
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            Type: {case_name}
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            status: {status}
            </Typography>
            <Typography variant="body2" component="p">
            date: {date_of_judgement}
            </Typography>
            <Typography variant="body2" component="p">
                {eligibility[0]
                    ? <Link
                    id={caseNum}
                    to={{
                        pathname: "/fill-form",
                        state: {
                            // res: this.props.all,
                            case_number: caseNum,
                            county_name: county_name,
                            case_name: case_name,
                            date_of_judgement: date_of_judgement,
                        },
                    }}
                    >
                    eligibility: {eligibility}
                    </Link>
                    : <p>eligibility: {eligibility}</p>
                }
            </Typography>
        </CardContent>
        </Card>
    </div>
    );
    }
}