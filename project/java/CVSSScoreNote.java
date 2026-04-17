package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Additional explanatory note for CVSS display conditions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CVSSScoreNote  {

  private String noteId;
  private String message;
  private String source;
  private ZonedDateTime created;

}