import React from 'react';
// import { makeStyles } from 'material-ui/core/styles';
import Card from '@material-ui/core/Card';
// import CardActions from 'material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
// import Button from 'material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import 'react-bootstrap';
import { Link } from "react-router-dom";

export default class SimpleCard extends React.Component{
    constructor(props) {
                super(props);
                this.state = {
                    caseNum: Object.keys(this.props.res),
                    result: this.props.res
                  };
    }
    render (){
    const {caseNum} = this.state;
    const {location: county_name, style: case_name , status, eligibility, date: date_of_judgement} = this.state.result[caseNum];

    return(
    <Container maxWidth="sm">
        <div className = "bg-light">
            <Card className='bg-light border'>
            <CardContent>
                <Typography className={caseNum+" text-center"} color="textSecondary" gutterBottom>
                Type: {case_name}
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                {caseNum} 
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                status: {status}
                </Typography>
                <Typography className={caseNum}  gutterBottom>
                Location: {county_name}
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
    </Container>
    );
    }
}