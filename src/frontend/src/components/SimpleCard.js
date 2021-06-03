import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
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
    const {location: county_name, style: case_name , status, eligibility, date: date_of_judgement, case_id} = this.state.result[caseNum];
    console.log("Id is; " + case_id)
    return(
    <Container maxWidth="sm">
        <div className = "bg-light">
            <Card className='bg-light border'>
            <CardContent>
                <Typography className={caseNum+" text-center"} color="textSecondary" gutterBottom>
                Case Name: {case_name}
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                {caseNum} 
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                Status: {status}
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                Location: {county_name}
                </Typography>
                <Typography variant="body2" component="p">
                Date: {date_of_judgement}
                </Typography>
                <Typography variant="body2" component="p">
                    <Button  size="small" style={{backgroundColor: "#4caf50"}}>
                            Eligible Now
                    </Button> : {eligibility}
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
                        <Button color="primary" variant="contained" size="small" href="/fill-form">Click to autofill application pdf</Button>    
                        </Link>
                        : <p>Eligibility:{eligibility}</p>
                    }
                </Typography>
                <CardActions>    
                </CardActions>
            </CardContent>
            </Card>
            <br></br>
        </div>  
    </Container>
    );
    }
}